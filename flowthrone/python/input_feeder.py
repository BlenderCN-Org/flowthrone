import cv2
import glog as log

""" Iterator class for loading images from a video. """
class VideoFeeder:
    def __init__(self, filename):
        self.cap = cv2.VideoCapture(filename)
        log.check(self.cap.isOpened())
        # If first 'grab' doesn't succeed, then we're done :(
        self._done = not self.cap.grab()

    def done(self):
        return self._done

    def next(self):
        log.check(not self._done, "Should check 'done()' prior to calling this function!")
            
        retval, image = self.cap.retrieve()
        log.check(retval, "Failed to grab error from video. This is a logical error in VideoFeeder")
        self._done = not self.cap.grab()
        return image

""" Iterator class for loading images from a list of image filenames """
class ImageFeeder:
    def __init__(self, filenames):
        self.filenames = filenames
        self._done = len(self.filenames) == 0

    def done(self):
        return self._done

    def next(self):
        log.check(not self._done, "Should check 'done()' prior to calling this function!")
        image = cv2.imread(self.filenames[0])
        self.filenames = self.filenames[1:]
        self._done = len(self.filenames) == 0
        return image


