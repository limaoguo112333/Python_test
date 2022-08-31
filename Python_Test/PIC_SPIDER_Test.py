# -*- coding: gbk -*-
#第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-) (这个链接已经炸了，换了一个)

import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import ssl
import re
import sys
import time

ssl._create_default_https_context = ssl._create_unverified_context

class Pic_Spider():
    def get_html(self, url):
        try:
            with urllib.request.urlopen(url) as f:      #打开并读取网页内容
                html = f.read().decode('utf-8')
            return html
        except urllib.error.URLError as e:      #网站打不开报错
            print(e.reason)
            sys.exit()

    def get_img(self, html):
        #imgre = BeautifulSoup(html, 'html.parser')
        #imglist = imgre.select('img')
        imgre = re.compile(r'src="(https.*?)"')     #匹配src内链接
        imglist = re.findall(imgre, html)
        print(imglist)
        i = 0
        datetime = time.strftime('%Y%m%d%H%M%S', time.localtime())      #获取当前时间
        for imgurl in imglist:
            i += 1
            urllib.request.urlretrieve(imgurl, '%s.jpg'%(datetime + str(i)))    #保存图片
            print(datetime, ':', imgurl)

        page = BeautifulSoup(html, 'html.parser')
        pagelist = page.select('a.nxt')     #提取下一页链接
        if pagelist == []:
            return i, 'end'
        else:
            return i, pagelist[-1].get('href')

if __name__ == '__main__':
    spider = Pic_Spider()
    url = 'https://www.qter.org/forum.php?mod=viewthread&tid=629'
    while url != 'end':
        html = spider.get_html(url)
        num, url = spider.get_img(html)
        print(num, 'pictures get')
