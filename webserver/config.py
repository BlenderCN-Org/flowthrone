import os

SERVER_PATH = os.path.dirname(os.path.abspath(__file__))
FLOWTHRONE_BUILD_PATH = os.path.join(os.path.split(SERVER_PATH)[0], 'build')
FLOWTHRONE_OPTIONS_PBTXT = os.path.join(
        FLOWTHRONE_BUILD_PATH, 'config', 'flowthrone.pbtxt')
ALLOWED_VIDEO_EXTENSIONS = ['mp4', 'avi']                                       
ALLOWED_IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'bmp', 'png']
MAX_CONTENT_LENGTH = 16 * 1024 * 1024 # 16 mb
SERVER_PATH = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(SERVER_PATH, 'uploads/')
OUTPUT_IMAGE_FILENAME = 'output.png'
OUTPUT_VIDEO_FILENAME = 'output.webm' # VP80 in opencv.
OUTPUT_LOG_FILENAME = 'output.log'

DEFAULT_OPTICAL_FLOW_OPTIONS = open(FLOWTHRONE_OPTIONS_PBTXT).read()

# Make the uploads directory if necessary.
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
