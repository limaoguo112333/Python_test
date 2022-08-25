# -*- coding: gbk -*-
#第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。

import os
import re

letter_list = {}

def letters_num(file):
    if not os.path.exists(file):    #判断文件是否存在
        print('The file does not exist!')
        return
    
    with open (file, 'rt', encoding = 'utf-8') as f:    #rt模式打开文件，由于有的英文文档里会出现中文符号，故使用utf-8编码打开，否则有乱码
        for line in f.readlines():  #读取文本并按行处理
            #多种分隔符分割，并去除\u200b，这里本来是用[^a-zA-Z]匹配的，但是发现如it's还有A.O.C.这种也会被分割
            letters_line = re.split(r'[,;\s"“”:]|\.\s|\u200b', line)
            for letter in letters_line:
                if letter in letter_list:   #统计单词数量
                    letter_list[letter] += 1
                else:
                    letter_list[letter] = 1
                    
    del letter_list[''] #否则结果中会有''的统计，感觉这个应该是不可见字符？
    letter_list_sorted = sorted(zip(letter_list.values(), letter_list.keys()))  #对换键值位置，按值排序
    letter_num = 0
    for i in letter_list_sorted:
        print(i)
        letter_num += i[0]
    print('Letter kinds:', len(letter_list))    #单词数
    print('Letter nums:', letter_num)   #单词个数

if __name__ == '__main__':
    file = 'F:\\Visual_Studio\\WorkSpace\\PYTHON_TEST\\LETTERS_TEST\\letter_test.txt'
    letters_num(file)

