#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys
import matplotlib.pyplot as plt
import numpy as np
filesize = np.arange(100, 1100, 100)
y = np. arange(1000, 11000, 1000)
plt.plot(filesize, y, color = 'b')
plt.show()
print(filesize)
#
# os.chdir("file_download")
# # 列出目录
# print("目录为: %s"%os.listdir(os.getcwd()))
# path = "/terrence/use/make"
# print(os.path.split(path))
# # 重命名
# # os.rename("file1.txt", "file2.txt")
#
# print("重命名成功。")
#
# # 列出重命名后的目录
# print("目录为: %s" %os.listdir(os.getcwd()))