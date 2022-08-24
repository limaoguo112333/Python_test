# -*- coding: gbk -*-
# 一个文件夹压缩程序

import os
import time
import zipfile

source = 'F:/Visual_Studio/WorkSpace/Line3DPlot'
target_dir = 'F:/Visual_Studio/WorkSpace'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y_%m_%d') #命名存放文件夹
now = time.strftime('Line3DPlot_%H_%M_%S')  #命名压缩文件
target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zipFile = zipfile.ZipFile(target, 'w')  #创建zipfile对象
for path, dirnames, filenames in os.walk(source): #逐层遍历所有子文件夹
        fpath = path.replace(source, '')
        for filename in filenames:
            zipFile.write(os.path.join(path, filename), os.path.join(fpath, filename))  #将每个文件写入zipfile对象下对应目录中
zipFile.close()
