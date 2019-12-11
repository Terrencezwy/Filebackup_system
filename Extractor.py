import os
import hashlib


def file_extractor(abspath):
    file_path = abspath
    file_name = os.path.basename(abspath)
    md5_code = md5conversion(abspath)
    file_size = os.path.getsize(abspath)
    file_type = 'File'

    print(file_size)
    # print()


def md5conversion(path):
    file = open(path, 'rb')
    md = hashlib.md5()
    md.update(file.read())
    return md.hexdigest()
    # print(md.hexdigest())