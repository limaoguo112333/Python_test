# -*- coding: gbk -*-
#第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
#所用图片：https://github.com/limaoguo112333/Python_test/blob/main/res/1506425.gif

from PIL import Image, ImageDraw, ImageFont
import random

def draw_to_pic(pics, num):
    pic = Image.open(pics)
    pic = pic.convert('RGBA') #这里由于测试用图像问题，需要转成RGBA，否则报错
    pic_draw = ImageDraw.Draw(pic)
    width, height = pic.size
    #print(width, height)
    #print(num)
    num_font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 10) #设置字体
    num_color = "#ff0000" #设置颜色，这里是红色
    pic_draw.text((width - 10, 10), '%s' % num, font = num_font, fill = num_color)
    pic.save('pic.png')

if __name__ == '__main__':
    pics = 'F:/Visual_Studio/WorkSpace/1506425.gif'
    draw_to_pic(pics, random.randint(1, 10))
