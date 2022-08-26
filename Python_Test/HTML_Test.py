# -*- coding: gbk -*-
#第 0008 题： 一个HTML文件，找出里面的正文。
#第 0009 题： 一个HTML文件，找出里面的链接。

from bs4 import BeautifulSoup
import os

def search_html(html_path):
    if not os.path.exists(html_path):
        print('文件路径错误')
        return

    with open(html_path, 'rt', encoding = 'utf-8') as f:
        html_note = f.read()
        soup = BeautifulSoup(html_note, 'html.parser')  #解析html文件
        print(soup.title)
        #print(soup.p)  #p标签内容
        urls = soup.find_all('a')
        for u in urls:
            print(u['href'])    #href属性用于指定超链接目标的url
        print(soup.find_all('body'))    #输出正文
        #print(soup.get_text)   #输出全文

if __name__ == '__main__':
    search_html('F:\\Visual_Studio\\WorkSpace\\Sources\\Yixiaohan_show-me-the-code_ Python.html')
