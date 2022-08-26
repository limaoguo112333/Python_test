# -*- coding: gbk -*-
#第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
#第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
#第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os
import re
from PIL import Image
from glob import glob
from os.path import join

class Menu_Bulk_Operations:
    #批量更改图片分辨率
    #查了一下，通常所说的分辨率即a*b形式的，指的是图片长*高方向上的像素数量
    #而水平、垂直分辨率即dpi，指的是每英寸内像素数量，可以理解为像素点密度
    #这里我们要修改的是前者
    def change_pic_size(self, pic_path, pic_save_path):
        if not os.path.exists(pic_path):
            print('图片路径不存在')
            return
        if not os.path.exists(pic_save_path):
            os.makedirs(pic_save_path)  #若存放目录不存在，则递归建立文件夹
        img_path = []
        for ext in ('*.jpg', '*.png', '*.gif'):     #匹配搜索目录下特定格式的文件
            img_path.extend(glob(join(pic_path, ext)))
        for pic_file in img_path:
            pic_name = os.path.join(pic_save_path, pic_file.split(os.sep)[-1])  #保存路径
            print(pic_name)
            pic = Image.open(pic_file)
            pic.thumbnail((1136, 640))  #保持长宽比更改分辨率，不超过1136*640
            try:    #这里遇到有的图片位深度是32，在保存为JPEG时会报错'cannot write mode RGBA as JPEG'，所以增加保存为PNG的选项
                pic.save(pic_name, 'JPEG')
            except:
                pic.save(pic_name, 'PNG')
        print('图片处理完毕')

    #批量统计文本内出现频率最高的词
    def letter_num_max(self, diary_path):
        if not os.path.exists(diary_path):
            print('文本路径不存在')
            return
        txt_path = glob(join(diary_path, '*.txt'))

        #这里直接用了LETTER_Test.py的代码，不过多注释
        #如果只需要统计出现频率最高的词汇，也可以直接用list的max方法
        for txt_file in txt_path:
            letter_list = {}
            with open(txt_file, 'rt', encoding = 'utf-8') as f:
                for line in f.readlines():
                    letters_line = re.split(r'[,;\s"“”:]|\.\s|\u200b', line)
                    for letter in letters_line:
                        if letter in letter_list:
                            letter_list[letter] += 1
                        else:
                            letter_list[letter] = 1
                    
            del letter_list['']     #这里也可以选择把a、the、of等一系列虚词去掉
            letter_list_sorted = sorted(zip(letter_list.values(), letter_list.keys()), reverse = True)
            print(txt_file + ':')
            for i in range(3):      #输出频率前三的词
                print('No.%d' % (i + 1), letter_list_sorted[i])


    #批量统计代码
    def codes_stat(self, codes_path):
        if not os.path.exists(codes_path):
            print('代码路径不存在')
            return
        code_path = glob(join(codes_path, '*.py'))

        code_line_num = 0
        space_line_num = 0
        anno_line_num = 0
        text_pat = '.*#'    #匹配单行注释。对于行内注释以及'''的多行注释没想出好的解决办法
        for code_file in code_path:
            codes = 0
            spaces = 0
            annos = 0
            with open(code_file, 'rt', encoding = 'utf-8') as f:
                for line in f.readlines():
                    code_line_num += 1
                    codes += 1
                    if line.isspace():  #判断空行
                        space_line_num += 1
                        spaces += 1
                    elif '#' in line and (re.findall(text_pat,line)[0][:-1].isspace() or re.findall(text_pat, line)[0][:-1] == ""):
                        anno_line_num += 1
                        annos += 1
            print(code_file, ':', end='\t')
            print('Codes:', codes, end=', ')
            print('Spaces:', spaces, end=', ')
            print('Annos:', annos)

        print('Code lines num:', code_line_num)
        print('Space lines num:', space_line_num)
        print('Annotation lines num:', anno_line_num)


if __name__ == '__main__':
    bulk_op = Menu_Bulk_Operations()
    comm = input('输入命令：（pic/text/code）')
    if comm == 'pic':
        bulk_op.change_pic_size('F:\\Visual_Studio\\WorkSpace\\Sources\\pics\\imgs', '.\\pics_result')
    elif comm == 'text':
        bulk_op.letter_num_max('F:\\Visual_Studio\\WorkSpace\\Sources\\articles')
    elif comm == 'code':
        bulk_op.codes_stat('F:\\Visual_Studio\\WorkSpace\\Sources\\codes')

