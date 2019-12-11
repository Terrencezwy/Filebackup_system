import Download_SFTP
import matplotlib.pyplot as plt
import Upload_SFTP_test
import numpy as np
import time


class Item:
    ID = None
    filePath_Client = None
    filePath_Server = None
    fileSize = None
    fileType = None
    fileName = None
    MD5 = None
    isExist_LastB = None
    isBp_complete = None

    def __init__(self, ID, filePath_Client, filePath_Server, fileSize, fileType, fileName, MD5, isExist_LastB,
                 isBp_complete):
        self.ID = ID
        self.filePath_Client = filePath_Client
        self.filePath_Server = filePath_Server
        self.fileSize = fileSize
        self.fileType = fileType
        self.fileName = fileName
        self.MD5 = MD5
        self.isExist_LastB = isExist_LastB
        self.isBp_complete = isBp_complete

    def print(obj):
        print(obj.__dict__)


if __name__ == "__main__":
    dim = 100
    cost_upload = np.zeros(10)
    cost_download = np.zeros(10)
    speed_upload = np.zeros(10)
    speed_download = np.zeros(10)
    """upload cost"""
    remotepath = '/file_backup_system_development/Efficiency_test'
    localpath = 'D:\\520project\\552project\\Efficiency_test'
    for i in range(10):
        start = time.clock()
        filename = 'Etest_%dMB.txt' % ((i + 1) * dim)
        # print(s)
        # print(os.path.join(localpath, s).replace('\\', '/'))
        # sftp.put(os.path.join(localpath, s).replace('\\', '/'), os.path.join(remotepath, s))
        Upload_SFTP_test.uploadhelper(remotepath, localpath, filename)
        cost_upload[i] = time.clock() - start
        print("time cost is:%f" % cost_upload[i])

    """Download cost"""
    for i in range(10):
        start = time.clock()
        filename2 = 'Etest_%dMB.txt' % ((i + 1) * dim)
        fileA = Item("001", "D:\\520project\\552project\\download_test",
                     "/file_backup_system_development/Efficiency_test/%s" % filename2,
                     "1206", "txt", filename2, "qwesadfasfaeadsfaf", False, True)
        Download_SFTP.downloadhelper(fileA)
        cost_download[i] = time.clock() - start

    fileSize = np.arange(dim, dim * 11, dim)
    speed_download = fileSize / cost_download
    speed_upload = fileSize / cost_upload
    """write the data into the log"""
    with open("AnalysisLog.txt", "a+") as f:
        for i in range(10):
            print("The file size is: %d MB" % fileSize[i])
            print("Upload Speed: %f MB/s" % speed_upload[i])
            print("Download Speed: %f MB/s" % speed_download[i])
            print("Upload time: %f s" % cost_upload[i])
            print("Download time: %f s" % cost_download[i])
            print('/n')
            print("The file size is: %d MB" % fileSize[i], file=f)
            print("Upload Speed: %f MB/s" % speed_upload[i], file=f)
            print("Download Speed: %f MB/s" % speed_download[i], file=f)
            print("Upload time: %f s" % cost_upload[i], file=f)
            print("Download time: %f s" % cost_download[i], file=f)
            print('/n', file=f)

    """PyPlot part"""
    plt.figure()
    plt.plot(fileSize, cost_upload, label="Upload cost", color='g')
    plt.plot(fileSize, cost_download, label='Download cost', color='r')
    plt.xlabel('file size(MB)')
    plt.ylabel('consuming time(s)')
    plt.title('time cost vs file size')
    plt.legend()
    plt.figure()
    plt.plot(fileSize, speed_upload, label='Upload speed', color='y')
    plt.plot(fileSize, speed_download, label='Download speed', color='b')
    plt.xlabel('file size (MB)')
    plt.ylabel('transmission speed (MB/s)')
    plt.title('transmission speed vs file size')
    plt.legend()
    plt.show()
