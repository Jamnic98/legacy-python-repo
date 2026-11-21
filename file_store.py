import os

from config import UPLOAD_DIR


def download(filename):
    f = open(os.path.join(UPLOAD_DIR, filename), "rb")
    data = f.read()
    f.close()
    return data


def save_upload(filename, data):
    f = open(os.path.join(UPLOAD_DIR, filename), "wb")
    f.write(data)
    f.close()
