import os
import Extractor


def file_scanner(path, prefix=''):
    if not os.path.exists(path):
        raise FileNotFoundError('Path %s not exist' % path)

    if os.path.isfile(path):
       # print(prefix+os.path.abspath(path))
       # print(os.path.basename(path))
        Extractor.file_extractor(os.path.abspath(path))
    elif os.path.isdir(path):
        #print(prefix+os.path.abspath(path))
        for it in os.scandir(path):
            file_scanner(it, '---'+prefix)

# Dir cannot be input md5

# One function that judge whether the whole path is changed using md5


if __name__== '__main__':
    # path = "/home/parallels/PycharmProjects"
    path = "C:\Users\TerrenceZwy\Desktop\study\maze runner"
    file_scanner(path)