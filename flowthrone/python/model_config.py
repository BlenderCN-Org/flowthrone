import os
import subprocess

MODELS_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'models')


class ModelPathHandle:
    def __init__(self, name, url):
        self.path = os.path.join(MODELS_PATH, name)
        self.name = name
        self.url = url

    def get_path(self):
        return self.path

    def load(self):
        if not os.path.exists(MODELS_PATH):
            print "Creating {}".format(MODELS_PATH)
            os.mkdir(MODELS_PATH)
        print "Downloading model {}".format(self.name)
        subprocess.check_call(
            ['wget', self.url, '-O', '/tmp/{}.zip'.format(self.name)])
        print "Unzipping model in {}".format(MODELS_PATH)
        subprocess.check_call(
            ['unzip', '/tmp/{}.zip'.format(self.name), '-d', MODELS_PATH])

    def load_if_needed(self):
        if not os.path.exists(MODELS_PATH) or not os.path.exists(self.path):
            self.load()
        return


MODELS = {
    'pwcnet_256x256_v0': ModelPathHandle(
        name='pwcnet_256x256_v0',
        url='https://www.dropbox.com/s/s4qscphc0lhbsmf/pwcnet_256x256_v0.zip?dl=0'
    ),
    'pwcnet_128x128_v1': ModelPathHandle(
        name='pwcnet_128x128_v1',
        url='https://www.dropbox.com/s/yii3xwrm7q8dc2z/pwcnet_256x256_v1.zip?dl=0',
    ),
}
