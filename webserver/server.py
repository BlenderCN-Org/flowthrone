from flask import Flask
from flask import flash, render_template, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
from flaskext.markdown import Markdown
import utils
import os
import config
import json
import flowthrone_pb2
import google.protobuf.text_format

app = Flask(__name__)
app.secret_key = 'secret'
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = config.MAX_CONTENT_LENGTH
app.config['TEMPLATES_AUTO_RELOAD'] = True
Markdown(app)


@app.route('/')
@app.route('/index.html')
def index():
    """ Front page """
    return render_template('index.html')


@app.route('/demo')
def demo():
    """ Demo page """
    return render_template(
        'demo.html', default_options_pbtxt=config.DEFAULT_OPTICAL_FLOW_OPTIONS)


@app.route('/examples')
def examples():
    """ Directory listing of runs that have been done. """
    uuids = [d for d in os.listdir(config.EXAMPLES_FOLDER) \
            if utils.result_is_valid(config.EXAMPLES_FOLDER, d)]
    uuids.sort()
    uuids.reverse()
    return render_template('examples.html', results=uuids)


@app.route('/docs')
def docs():
    """ Documentation page """
    return render_template('docs.html')


def internal_error():
    """ Shorthand for reporting catasrophes. """
    return render_template(
        'response.html', content='Internal error', error=True)


@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    """ View for content that's been uploaded. """
    return send_from_directory(config.UPLOAD_FOLDER, filename)


@app.route('/submit_task', methods=['POST'])
def submit_task():
    if not request.method == 'POST':
        return index()

    # Check that the user provided two valid images or a video.
    valid, error_msg = utils.request_is_valid(request)
    if not valid:
        return render_template('response.html', content=error_msg, error=True)

    # Task is valid, so schedule it and return the identifier.
    task_uuid = utils.schedule_task(request, config.EXAMPLES_FOLDER)
    if not task_uuid:
        return internal_error()

    success_msg = ("Successfully uploaded files and scheduled a task '{}'."
                   ).format(task_uuid)
    return render_template('response.html', content=success_msg, error=False)


@app.route('/results')
def results():
    results = [f for f in os.listdir(config.RESULTS_FOLDER) \
        if os.path.isdir(os.path.join(config.RESULTS_FOLDER, f))]
    results.sort()
    return render_template('results.html', results=results)


@app.route('/result/<result_id>')
def result(result_id):
    p = os.path.join(config.RESULTS_FOLDER, result_id)
    result_pbtxt = [
        os.path.join(p, f) for f in os.listdir(p) if f.endswith('pbtxt')
    ][0]
    stats = utils.read_evaluation_results_pbtxt(result_pbtxt)

    return render_template('result.html', stats=stats, result_id=result_id)


@app.route('/delete_example/<result_id>')
def delete_example(result_id, methods=['GET']):
    utils.delete_result(config.EXAMPLES_FOLDER, result_id)
    return index()


@app.route('/load_example/<result_id>')
def load_example(result_id):
    """ Returns a JSON with results for a given id. """
    result_data = {
        'id': result_id,
        'stderr': '',
        'result_image_filename': '',
        'result_video_filename': '',
    }

    result_image_filename = utils.result_image_filename_or_none(
        config.EXAMPLES_FOLDER, result_id)
    result_video_filename = utils.result_video_filename_or_none(
        config.EXAMPLES_FOLDER, result_id)
    result_stderr_filename = utils.result_stderr_filename_or_none(
        config.EXAMPLES_FOLDER, result_id)

    if result_stderr_filename is not None:
        full_filename = os.path.join(config.EXAMPLES_FOLDER,
                                     result_stderr_filename)
        result_data['stderr'] = open(full_filename).read()
    if result_image_filename is not None:
        result_data['result_image_filename'] = os.path.join(
            'examples', result_image_filename)
    if result_video_filename is not None:
        result_data['result_video_filename'] = os.path.join(
            'examples', result_video_filename)

    return json.dumps(result_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
