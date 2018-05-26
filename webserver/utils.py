import os
from werkzeug.utils import secure_filename
import config
import base64
import time
import subprocess
import uuid
import shutil


def file_is_allowed(filename, allowed_extensions):
    return any([filename.lower().endswith(ext.lower()) \
        for ext in allowed_extensions])


def request_has_valid_images(files):
    """ Returns a pair (True/False, error message). """
    # check if images are specified.
    for k in ['image1', 'image2']:
        if k not in files or files[k].filename == '' or not files[k]:
            return False, 'One or more images were not specified.'
    # if both images are specified, ensure that they have valid extensions
    for k in ['image1', 'image2']:
        if not file_is_allowed(files[k].filename,
                               config.ALLOWED_IMAGE_EXTENSIONS):
            return False, \
                "Image was specified: '{}', but is not an allowed file.".format(
                    files[k].filename)
    return True, ''

def request_has_valid_url(url):
    if len(url) == 0:
        return False, "URL was not specified"
    is_downloadable = is_downloadable_url(url)
    if is_downloadable:
        return True, ''
    else:
        return False, "URL was specified, but is not downloadable."

def request_has_valid_video(files):
    """ Returns a pair (True/False, error message). """
    # check if video is specified.
    if 'video' not in files or files['video'].filename == '' or not files['video']:
        return False, 'Video was not specified.'
    if not file_is_allowed(files['video'].filename,
                           config.ALLOWED_VIDEO_EXTENSIONS):
        return False, \
            "Video was specified: '{}', but is not an allowed file.".format(
                files['video'].filename)
    return True, ''


def request_is_valid(request):
    """ Returns a pair (True/False, error message). """
    has_url, err_url = request_has_valid_url(request.form['video-url'])
    has_images, err_images = request_has_valid_images(request.files)
    has_video, err_video = request_has_valid_video(request.files)

    if sum([has_images, has_video, has_url]) > 1:
        return False, ("Please only specify either a single url, or a pair of images or a video -- request is ambiguous otherwise!")
    if sum([has_images, has_video, has_url]) == 0:
        return False, '\n'.join([err_images, err_video, err_url])
    return True, ''


def upload_file(file, upload_folder):
    filename = os.path.join(upload_folder, secure_filename(file.filename))
    file.save(filename)
    return filename

def is_downloadable_url(url):
    import youtube_dl
    ydl = youtube_dl.YoutubeDL({})
    try:
        print "Attempting to extract info from ", url
        info = ydl.extract_info(url, download=False)
        print info
        return True
    except:
        print "Caught exception: ", str(e)
        return False

def upload_youtube_url(url, upload_folder):
    import youtube_dl
    ydl_opts = {
            'outtmpl': os.path.join(upload_folder, 'video.%(ext)s'),
            'keepvideo': True,
            'merge_output_format': 'mkv',
            }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download([url])
    return os.path.join(upload_folder, 'video.mkv')



def upload_files(request, upload_folder):
    """ Uploads and returns a list of uploaded files. If images were sent, the
    list will have two elements; otherwise it will be a singleton.
    The user must check that the request is valid prior to running this.
    """
    uploaded_files = []
    has_images, _ = request_has_valid_images(request.files)
    if has_images:
        return [
            upload_file(request.files['image1'], upload_folder),
            upload_file(request.files['image2'], upload_folder)
        ]

    has_video, _ = request_has_valid_video(request.files)
    if has_video:
        return [upload_file(request.files['video'], upload_folder)]

    has_url, _ = request_has_valid_url(request.form['video-url'])
    if has_url:
        return [upload_youtube_url(request.form['video-url'], upload_folder)]

def upload_options_pbtxt(request, output_filename):
    # TODO: check that pbtxt is valid.
    with open(output_filename, 'w') as fid:
        fid.write(request.form['flowthroneoptions'])


def optical_flow_binary():
    return os.path.join(config.FLOWTHRONE_BUILD_PATH, './optical_flow_tool')


def get_optical_flow_tool_images_command(img1_filename, img2_filename,
                                         options_pbtxt_filename,
                                         output_filename, output_log_filename):
    return [
        optical_flow_binary(), '--img1', img1_filename, '--img2',
        img2_filename, '--options', options_pbtxt_filename, '--output',
        output_filename, '--alsologtostderr=1', '&>', output_log_filename
    ]


def get_optical_flow_tool_video_command(video_filename, options_pbtxt_filename,
                                        output_filename, output_log_filename):
    MAX_INPUT_DIM = 320*2 # resize videos that are larger than this value.
    LEAST_FLOW_MAGNITUDE = 10.0 # leads to slightly better looking results.
    return [
        optical_flow_binary(), '--video', video_filename, '--options',
        options_pbtxt_filename, '--output', output_filename,
        '--max_input_dim', str(MAX_INPUT_DIM),
        '--vis_least_flow_magnitude', str(LEAST_FLOW_MAGNITUDE),
        '--alsologtostderr=1', '&>', output_log_filename
    ]


def get_optical_flow_tool_command(input_files, options_pbtxt_filename,
                                  output_filename, output_log_filename):
    if len(input_files) == 2:
        # Must be a pair of images then!
        return get_optical_flow_tool_images_command(
            input_files[0], input_files[1], options_pbtxt_filename,
            output_filename, output_log_filename)
    if len(input_files) == 1:
        return get_optical_flow_tool_video_command(
            input_files[0], options_pbtxt_filename, output_filename,
            output_log_filename)
    return None


def result_filename_or_none(upload_folder, result_id, match):
    """ Checks for files in `upload_folder/result_id/match` and returns
        'result_id/match' (if there is a unique match). """
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


def delete_result(upload_folder, result_id):
    if not result_id in os.listdir(upload_folder):
        print "Could not delete {} (doesn't exist? in {})".format(
            result_id, upload_folder)
    p = os.path.join(upload_folder, result_id)
    shutil.rmtree(p, ignore_errors=True)


def base64_encoded_image(image_bytes, ext):
    return 'data:image/' + ext + ';base64,' + base64.b64encode(image_bytes)


def task_identifier():
    t = time.time()
    return '{:10d}-{}'.format(long(t), uuid.uuid1(clock_seq=long(t)).hex[0:8])


def convert_avi_to_webm(input_filename, output_filename):
    cmd = [
        'ffmpeg',
        '-i',
        input_filename,
        '-c:v',
        'libvpx',
        '-qmin',
        str(0),
        '-qmax',
        str(1),
        '-crf',
        str(1),
        '-q:v',
        '1',
        output_filename,
    ]
    print cmd
    subprocess.call(cmd)


def schedule_task(request, upload_folder):
    """ Schedules a task and returns an id on success, and 'None' on failure. """
    task_uuid = task_identifier()
    task_folder = os.path.join(upload_folder, task_uuid)
    if not os.path.exists(task_folder):
        try:
            os.mkdir(task_folder)
        except:
            print "Could not create {}".format(task_folder)
            return None

    options_pbtxt = os.path.join(task_folder, 'options.pbtxt')
    upload_options_pbtxt(request, options_pbtxt)

    uploaded_files = upload_files(request, task_folder)
    if len(uploaded_files) == 2:
        output_filename = os.path.join(task_folder,
                                       config.OUTPUT_IMAGE_FILENAME)
    else:
        output_filename = os.path.join(task_folder,
                                       config.OUTPUT_VIDEO_FILENAME)
        # Opencv is unbelievably frustrating. Even with ffmpeg built from
        # source with libvpx support, opening a video for writing fails.
        # Instead, first write an 'avi' file, and then convert it to webm
        # below.
        output_filename = output_filename.replace('webm', 'avi')
    output_log_filename = os.path.join(task_folder, config.OUTPUT_LOG_FILENAME)
    cmd = get_optical_flow_tool_command(uploaded_files, options_pbtxt,
                                        output_filename, output_log_filename)
    # This is really bad, since it will:
    #   (a) block the website until everything is done.
    #   (b) multiple users accessing the website simultaneously will crash the
    #       whole system (at best, something will OOM).
    # It would have been much better to either:
    #   (a) launch the task with Celery
    #   (b) launch it async with popen
    print cmd
    with open(output_log_filename, 'w') as f:
        subprocess.call(cmd, stdout=f, stderr=f)

    if output_filename.endswith('avi'):
        convert_avi_to_webm(output_filename,
                            output_filename.replace('avi', 'webm'))
    return task_uuid


def read_evaluation_results_pbtxt(filename):
    """ Parses pbtxt file and returns EvaluationOutput message. """
    import flowthrone_pb2
    import google.protobuf.text_format
    result_str = open(filename, 'r').read()
    stats = flowthrone_pb2.EvaluationOutput()
    google.protobuf.text_format.Merge(result_str, stats)
    return stats
