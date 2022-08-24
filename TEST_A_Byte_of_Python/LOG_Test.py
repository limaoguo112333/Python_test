# -*- coding: gbk -*-
# 一段输出日志文件的代码

import os
import platform
import logging

if platform.platform().startswith('Windows'): #将日志文件存放在系统目录
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')

print("Logging to", logging_file)

logging.basicConfig(
    level = logging.DEBUG,  #设置日志级别
    format = '%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w',
)

#输出
logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")
