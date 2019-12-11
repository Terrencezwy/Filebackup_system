import paramiko
import os
import numpy as np
import time
import matplotlib.pyplot as plt


def upload_from_client(sftp_obj, remote_dir_path, local_dir_path, file_name):
    remote_dir_path = os.path.join(remote_dir_path, file_name)
    remote_dir_path = remote_dir_path.replace("\\", '/')
    print(remote_dir_path)
    local_dir_path = os.path.join(local_dir_path, file_name)
    print("start uploading file:" + file_name)
    sftp_obj.put(local_dir_path, remote_dir_path)


def uploadhelper(remote_path, local_path, file_name):
    """ server connection information"""
    host_name = ''
    # user_name = ''
    # password = '
    user_name = ''
    password = ''
    port = 22

    """connect to the remote server"""
    t = paramiko.Transport((host_name, port))
    t.connect(username=user_name, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    """upload files"""
    upload_from_client(sftp, remote_path, local_path, file_name)

    t.close()


# sftp.chdir('/root/file_backup_system/Efficiency_test')


if __name__ == "__main__":
    remotepath = '/file_backup_system_development/Efficiency_test'
    localpath = 'D:\\520project\\552project\\Efficiency_test2'
    cost = np.zeros(10)
    for i in range(10):
        start = time.clock()
        filename = "Etest_%dMB.txt" % ((i + 1) * 10)
        # print(s)
        # print(os.path.join(localpath, s).replace('\\', '/'))
        # sftp.put(os.path.join(localpath, s).replace('\\', '/'), os.path.join(remotepath, s))
        uploadhelper(remotepath, localpath, filename)
        cost[i] = time.clock() - start
        print("time cost is:%f" % cost[i])
    """PyPlot part"""
    fileSize = np.arange(10, 110, 10)
    plt.plot(fileSize, cost, label = "Upload cost")
    plt.xlabel('file size')
    plt.ylabel('Upload time')
    plt.title('Upload cost vs file size')
    plt.legend()
    plt.show()

# remotepath = remotepath.replace('\\', '/')
# localpath = localpath.replace('\\', '/')
# sftp.put(localpath, remotepath)
# sftp.put(localpath)
