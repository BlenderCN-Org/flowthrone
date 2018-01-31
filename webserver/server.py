from flask import Flask
from flask import flash, render_template, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
import utils
import os
import config
import json

app = Flask(__name__)
app.secret_key = 'secret'
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = config.MAX_CONTENT_LENGTH

""" Front page """
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

""" Demo page """
@app.route('/demo')
def demo():
    return render_template('demo.html', 
        default_options_pbtxt=config.DEFAULT_OPTICAL_FLOW_OPTIONS)

""" Directory listing of runs that have been done. """
@app.route('/examples')
def examples():
    uuids = [d for d in os.listdir(app.config['UPLOAD_FOLDER']) \
            if utils.result_is_valid(app.config['UPLOAD_FOLDER'], d)]
    uuids.sort()
    uuids.reverse()
    return render_template('examples.html', results=uuids)

""" Documentation page """
@app.route('/docs')
def docs():
    return render_template('docs.html')

""" Shorthand for reporting catasrophes. """
def internal_error():
    return render_template('response.html', content='Internal error', error=True)

""" View for content that's been uploaded. """
@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/submit_task', methods=['POST'])
def submit_task():
    if not request.method == 'POST':
        return index()
    
    # Check that the user provided two valid images or a video.
    valid, error_msg = utils.request_is_valid(request)
    if not valid:
        return render_template('response.html', content=error_msg, error=True) 
    
    # Task is valid, so schedule it and return the identifier.
    task_uuid = utils.schedule_task(request, app.config['UPLOAD_FOLDER'])
    if not task_uuid:
        return internal_error()

    success_msg = ("Successfully uploaded files and scheduled a task '{}'.").format(task_uuid)
    return render_template('response.html', content=success_msg, error=False)

""" Returns a JSON with results for a given id. """
@app.route('/load_example/<result_id>')
def load_example(result_id):
    result_data = {
        'id': result_id,
        'stderr': '',
        'result_image_filename': '',
        'result_video_filename': '',
    }
    
    result_image_filename = utils.result_image_filename_or_none(
            app.config['UPLOAD_FOLDER'], result_id)
    result_video_filename = utils.result_video_filename_or_none(
            app.config['UPLOAD_FOLDER'], result_id)
    result_stderr_filename = utils.result_stderr_filename_or_none(
            app.config['UPLOAD_FOLDER'], result_id)
   
    if result_stderr_filename is not None:
        full_filename = os.path.join(
            app.config['UPLOAD_FOLDER'], result_stderr_filename)
        result_data['stderr'] = open(full_filename).read()
    if result_image_filename is not None: 
        result_data['result_image_filename'] = result_image_filename
    if result_video_filename is not None: 
        result_data['result_video_filename'] = result_video_filename

    return json.dumps(result_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

