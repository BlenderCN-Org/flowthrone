import os
import subprocess
import glog as log
import tempfile

# Path to where models are downloaded and stored.
MODELS_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'models')


class ModelPathRegistry:
    """
    Wrapper around models paths / locations that's meant to abstract away how
    models are stored by the library from how the user can find them.

    USAGE:
    >>> local_model_path = ModelPathRegistry().get_latest()

    This will download the model from some remote storage (dropbox, yay),
    save it to the disk, and will give you a local path. Downloading is done
    only the first time around.
    Most users should only care about the latest model. It is also possible
    to load models by name, e.g:

    >>> for model in ModelPathRegistry().list():
    >>>    local_model_path = ModelPathRegistry().get(name)
    >>>    # do something with |local_model_path|
    """

    def __init__(self):
        self._latest_name = 'pwcnet_256x256_v3'
        self._models = {}

        # Below is a listing of all available models.
        urls = [
            """
            Model was trained on 20190406, on FlyingChairs2/SDHomChairs, without
            batch norm and without occlusion outputs.
            """
            'https://www.dropbox.com/s/29285l9pwwxzyai/pwcnet_256x256_v3.zip?dl',
        ]
        for url in urls:
            name = os.path.basename(url).split('.zip', 1)[0]
            self._models[name] = ModelPathHandle(
                name=name, url=url, local_dir=MODELS_PATH)

    def get(self, name):
        """ Returns a *path* to a specified model. """
        model_handle = self._models[name]
        model_handle.load_if_needed()
        return model_handle.get_path()

    def list(self):
        """ Lists all available model *names*. """
        return [k for k in self._models]

    def get_latest(self):
        """ Returns the *path* to the latest and greatest model. """
        return self.get(self._latest_name)

    def get_latest_name(self):
        """ Returns the *name* of the latest and greatest model. """
        return self._latest_name


class ModelPathHandle:
    def __init__(self, name, url, local_dir):
        self.name = name
        self.path = os.path.join(local_dir, name)
        self.url = url
        self.local_dir = local_dir

    def get_path(self):
        return self.path

    def load(self):
        if not os.path.exists(self.local_dir):
            print "Creating {}".format(self.local_dir)
            os.mkdir(self.local_dir)
        tmp_filename = tempfile.mkstemp()[1] + '.zip'
        print "Downloading model {} to {}".format(self.name, tmp_filename)
        if self.url.startswith('http'):
            subprocess.check_call(['wget', self.url, '-O', tmp_filename])
        elif os.path.exists(self.url):
            subprocess.check_call(['cp', self.url, tmp_filename])
        print "Unzipping model in {}".format(self.local_dir)
        subprocess.check_call(['unzip', tmp_filename, '-d', self.local_dir])
        os.remove(tmp_filename)

    def _need_load(self):
        return not os.path.exists(self.local_dir) or not os.path.exists(
            self.path)

    def load_if_needed(self):
        if self._need_load():
            self.load()
        log.check(
            not self._need_load(),
            message='Has just downloaded the model, but need to download '
            'it again. Something went wrong -- maybe downloaded it to '
            'the wrong location instead of {}?'.format(self.path))
