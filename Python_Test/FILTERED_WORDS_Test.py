# -*- coding: gbk -*-
#第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
#第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
'''
    北京
    程序员
    公务员
    领导
    牛比
    牛逼
    你娘
    你妈
    love
    sex
    jiangge
'''

import os
import sys
from threading import Thread

class Find_Filtered_Words():
    f_words = ''

    #为了不反复读取文件，将其单独写成函数
    def open_text(self, text_path):
        if not os.path.exists(text_path):
            print('文件路径不存在')
            return 0
        with open(text_path, 'rt', encoding = 'utf-8') as f:    #按行读取文件并去掉换行符
            self.f_words = f.read().splitlines()
            #print(self.f_words)
        return 1

    def find_filtered_words(self, str_in):
        str_out = str_in
        for word in self.f_words:   #将屏蔽词库中的词语与输入字符串比对
            #print(word)
            if word in str_in:
                str_out = str_out.replace(word, '*' * len(word))    #将屏蔽词替换为*

        if str_out == str_in:
            print('Human Rights!!!')
        else:
            print('Freedom!!!')

        return str_out  #返回和谐后的字符串

if __name__ == '__main__':
    find_fwords = Find_Filtered_Words()
    if not find_fwords.open_text('C:\\Users\\admin\\Desktop\\filtered_words.txt'):
        sys.exit()
    while True:
        w = find_fwords.find_filtered_words(input('> 输入你的昵称：'))
        ans = input('确定使用昵称%s吗？（y/n）' % w)
        if ans == 'y' or ans == '':
            print('好的', w)
            break
        elif ans == 'e':
            break
        else:
            continue
