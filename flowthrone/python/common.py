import cv2
import os
import paramiko
import numpy as np


def remote_imread(uri,
                  flags=cv2.CV_LOAD_IMAGE_COLOR,
                  username=os.getenv('USER'),
                  password=None):
    """ Like cv2.imread, but for reading images from a remote machine:
            img = remote_imread('192.168.0.10:/home/whoami/image.jpg')
        If usernames do not match across local and remote machines, or if you
        do not have passwordless SSH, you may addionally specify credentials:
            img = remote_imread('192.168.0.10:/home/whoami/image.jpg',
                                usename='mallory',
                                password='12345678')
    """
    splits = uri.split(':')
    if not len(splits) == 2:
        raise ValueError('Provided filename must have a single colon, used '
                         'as a separator between hostname and the filename ')
    hostname = splits[0]
    img_fn = splits[1]

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(
        hostname, port=22, username=username, password=password, timeout=5)
    sftp = s.open_sftp()
    remote_file = sftp.open(img_fn)
    return cv2.imdecode(
        np.fromstring(remote_file.read(), np.uint8, count=-1), flags)
