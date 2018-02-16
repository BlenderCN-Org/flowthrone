import os
from werkzeug.utils import secure_filename
import config
import base64
import time
import subprocess
import uuid

def file_is_allowed(filename, allowed_extensions):
    return any([filename.lower().endswith(ext.lower()) \
        for ext in allowed_extensions])

""" Returns a pair (True/False, error message). """
def request_has_valid_images(files):
    # check if images are specified.
    for k in ['image1', 'image2']:
        if k not in files or files[k].filename == '' or not files[k]:
            return False, 'One or more images were not specified.'
    # if both images are specified, ensure that they have valid extensions 
    for k in ['image1', 'image2']:
        if not file_is_allowed(files[k].filename, config.ALLOWED_IMAGE_EXTENSIONS):
            return False, \
                "Image was specified: '{}', but is not an allowed file.".format(
                    files[k].filename)
    return True, ''

""" Returns a pair (True/False, error message). """
def request_has_valid_video(files):
    # check if video is specified.
    if 'video' not in files or files['video'].filename == '' or not files['video']:
        return False, 'Video was not specified.'
    if not file_is_allowed(files['video'].filename, config.ALLOWED_VIDEO_EXTENSIONS):
        return False, \
            "Video was specified: '{}', but is not an allowed file.".format(
                files['video'].filename)
    return True, ''

""" Returns a pair (True/False, error message). """
def request_is_valid(request):
    has_images, err_images = request_has_valid_images(request.files)
    has_video, err_video = request_has_valid_video(request.files)
    
    if has_images and has_video:
        return False, ("Specifying both a pair of images and a video is "
                       "ambiguous -- should specify only one.")
    if not has_images and not has_video:
        return False, '\n'.join([err_images, err_video])
    return True, '' 

def upload_file(file, upload_folder):
    filename = os.path.join(upload_folder, secure_filename(file.filename))
    file.save(filename)
    return filename

""" Uploads and returns a list of uploaded files. If images were sent, the
    list will have two elements; otherwise it will be a singleton. 
    The user must check that the request is valid prior to running this.
    """
def upload_files(request, upload_folder):
    uploaded_files = []
    has_images, _ = request_has_valid_images(request.files)
    if has_images:
        return [upload_file(request.files['image1'], upload_folder),
                upload_file(request.files['image2'], upload_folder)]
    
    has_video, _ = request_has_valid_video(request.files)
    if has_video:
        return [upload_file(request.files['video'], upload_folder)]

def upload_options_pbtxt(request, output_filename):
    # TODO: check that pbtxt is valid.
    with open(output_filename,'w') as fid:
        fid.write(request.form['flowthroneoptions'])


def optical_flow_binary():
    return os.path.join(config.FLOWTHRONE_BUILD_PATH, './optical_flow_tool')


def get_optical_flow_tool_images_command(img1_filename, img2_filename, 
        options_pbtxt_filename, output_filename, output_log_filename):
    return [optical_flow_binary(), 
        '--img1', img1_filename, '--img2', img2_filename,
        '--options', options_pbtxt_filename, 
        '--output', output_filename,
        '--alsologtostderr=1', '&>', output_log_filename]


def get_optical_flow_tool_video_command(video_filename, 
        options_pbtxt_filename, output_filename, output_log_filename):
    return [
        optical_flow_binary(), 
        '--video', video_filename,
        '--options', options_pbtxt_filename, 
        '--output', output_filename,
        '--alsologtostderr=1', '&>', output_log_filename]


def get_optical_flow_tool_command(input_files, options_pbtxt_filename, output_filename, output_log_filename):
    if len(input_files) == 2:
        # Must be a pair of images then!
        return get_optical_flow_tool_images_command(
            input_files[0], input_files[1], options_pbtxt_filename, output_filename, output_log_filename)
    if len(input_files) == 1:
        return get_optical_flow_tool_video_command(
            input_files[0], options_pbtxt_filename, output_filename, output_log_filename)
    return None 


""" Checks for files in `upload_folder/result_id/match` and returns
    'result_id/match' (if there is a unique match). """
def result_filename_or_none(upload_folder, result_id, match):
    if not result_id in os.listdir(upload_folder):
        return None
    files = os.listdir(os.path.join(upload_folder, result_id))
    filenames = [os.path.join(result_id, f) for f in files if f == match]
    if len(filenames) == 1:
        return filenames[0]
    else:
        return None

def result_image_filename_or_none(upload_folder, result_id):
    return result_filename_or_none(\
        upload_folder, result_id, config.OUTPUT_IMAGE_FILENAME)


def result_video_filename_or_none(upload_folder, result_id):
    return result_filename_or_none(\
        upload_folder, result_id, config.OUTPUT_VIDEO_FILENAME)


def result_stderr_filename_or_none(upload_folder, result_id):
    return result_filename_or_none(\
        upload_folder, result_id, config.OUTPUT_LOG_FILENAME)


def result_is_valid(upload_folder, result_id):
    if not result_id in os.listdir(upload_folder):
        return False
    
    files = os.listdir(os.path.join(upload_folder, result_id))
    log_filenames = [f for f in files if f == config.OUTPUT_LOG_FILENAME]
    # It is permissible not to have an output image/video. As long as the log
    # has been generated, let's say that the result is valid.
    return len(log_filenames) == 1

def base64_encoded_image(image_bytes, ext):
    return 'data:image/' + ext + ';base64,' + base64.b64encode(image_bytes)

def task_identifier():
    t = time.time()
    return '{:10d}-{}'.format(long(t), uuid.uuid1(clock_seq=long(t)).hex[0:8])

""" Schedules a task and returns an id on success, and 'None' on failure. """
def schedule_task(request, upload_folder):
    task_uuid = task_identifier()
    task_folder = os.path.join(upload_folder, task_uuid)
    try:
        os.mkdir(task_folder)
    except:
        return None
    options_pbtxt = os.path.join(task_folder, 'options.pbtxt')
    upload_options_pbtxt(request, options_pbtxt)
    
    uploaded_files = upload_files(request, task_folder)
    if len(uploaded_files) == 2:
        output_filename = os.path.join(task_folder, config.OUTPUT_IMAGE_FILENAME)
    else:
        output_filename = os.path.join(task_folder, config.OUTPUT_VIDEO_FILENAME)
    output_log_filename = os.path.join(task_folder, config.OUTPUT_LOG_FILENAME)
    cmd = get_optical_flow_tool_command(uploaded_files, options_pbtxt, output_filename, output_log_filename)
    print cmd
    # This is really bad, since it will:
    #   (a) block the website until everything is done.
    #   (b) multiple users accessing the website simultaneously will crash the
    #       whole system (at best, something will OOM).
    # It would have been much better to either:
    #   (a) launch the task with Celery
    #   (b) launch it async with popen
    with open(output_log_filename, 'w') as f:
        subprocess.call(cmd, stdout=f, stderr=f)
    return task_uuid 

""" Parses pbtxt file and returns EvaluationOutput message. """
def read_evaluation_results_pbtxt(filename):
    import flowthrone_pb2
    import google.protobuf.text_format
    result_str = open(filename, 'r').read()
    stats = flowthrone_pb2.EvaluationOutput()
    google.protobuf.text_format.Merge(result_str, stats)
    return stats
