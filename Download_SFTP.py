#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import os
import sys
from stat import S_ISDIR as isdir


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


def check_local_dir(local_dir_name):
    """find if the local file folder exist, if not then create"""
    if not os.path.exists(local_dir_name):
        os.makedirs(local_dir_name)
        print("mkdir success")


def renamefile(filename_at_server, filename_at_client):
    os.rename(filename_at_server, filename_at_client)
    print("rename successfully")


def down_from_remote(sftp_obj, remote_dir_path, local_dir_path, filename_at_client):
    """download from remote"""

    remote_file = sftp_obj.stat(remote_dir_path)
    """check if is folder"""
    if isdir(remote_file.st_mode):
        #file_list = fetch_folder_name(parent_folder)
        #for i in file_list
            #download_from_remote(sftp_obj, i.filePath_Server, i.filePath_Client, i.fileName)
        print("本地路径:" + local_dir_path)
        print("文件夹名称：" + filename_at_client)
        print(os.path.join(local_dir_path,filename_at_client))
        local_dir_path = os.path.join(local_dir_path, filename_at_client)
        check_local_dir(local_dir_path)
        print('start downloading the folder：' + remote_dir_path)

        for remote_file_name in sftp_obj.listdir(remote_dir_path):
            sub_remote = os.path.join(remote_dir_path, remote_file_name)
            sub_remote = sub_remote.replace('\\', '/')
            print(remote_file_name)
            # sub_local = os.path.join(local_dir_path, remote_file_name)
            # sub_local = sub_local.replace('\\', '/')

            # down_from_remote(sftp_obj, sub_remote, sub_local, remote_file_name)
            down_from_remote(sftp_obj, sub_remote, local_dir_path, remote_file_name)



        """if it is file"""
    else:
        check_local_dir(local_dir_path)
        print('start downloading the file：' + remote_dir_path)
        sub_remote = remote_dir_path.replace('\\', '/')
        # print(local_dir_path+"\\"+filename_at_client)
        local_dir_path = os.path.join(local_dir_path, filename_at_client)
        # local_dir_path = local_dir_path + "\\" + filename_at_client
        # local_dir_path = os.path.join(os.path.split(local_dir_path)[0], filename_at_client)
        local_dir_path = local_dir_path.replace('\\', '/')
        print(local_dir_path)
        sftp_obj.get(sub_remote, local_dir_path)


def downloadhelper(Item):
    """ server connection information"""
    host_name = ''
    user_name = ''
    password = ''
    port = 22

    """connect to the remote server"""
    t = paramiko.Transport((host_name, port))
    t.connect(username=user_name, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    # download the remote file
    # print(sftp.stat(remote_dir))
    # down_from_remote(sftp, Item.filePath_Server, os.path.split(Item.filePath_Client)[0], Item.fileName)
    down_from_remote(sftp, Item.filePath_Server, Item.filePath_Client, Item.fileName)

    """close the connection"""
    t.close()


if __name__ == "__main__":
    """test file"""
    # fileA = Item("001", "D:\\520project\\552project\\file_backup_system_development",
    #              "/file_backup_system_development/file1201.txt",
    #              "1206", "txt", "file1210.txt", "qwesadfasfaeadsfaf", False, True)
    # downloadhelper(fileA)
    """test folder"""
    fileA = Item("001", "D:\\520project\\552project",
                 "/file_backup_system_development",
                 "1206", "txt", "file_backup_system_development", "qwesadfasfaeadsfaf", False, True)
    downloadhelper(fileA)
    """download one file"""
    # downloadhelper('/file_backup_system_development/file1201.txt', 'D:\\520project\\552project\\file_download\\', 'file1201.txt')

    # downloadhelper('/file_backup_system_development', 'D:\\520project\\552project\\file_download\\', 'file1201.txt')

