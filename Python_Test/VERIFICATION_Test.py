# -*- coding: gbk -*-
#第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片

from PIL import Image, ImageFont, ImageDraw
import random

class Gen_Verification_Code():
    def get_random_color(self):     #随机生成颜色
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def get_random_str(self):       #随机生成字符
        num = str(random.randint(0, 9))
        low_alpha = chr(random.randint(97, 122))
        high_alpha = chr(random.randint(65, 90))
        str_random = random.choice([num, low_alpha, high_alpha])
        return str_random

    def gen_veri_code(self):
        img = Image.new('RGB', (150, 30), self.get_random_color())  #生成随机颜色背景图片
        draw = ImageDraw.Draw(img)
        str_font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', size = 26)
        for i in range(5):      #加入5个随机颜色字符
            draw.text((10 + i * 30, 0), self.get_random_str(), self.get_random_color(), font = str_font)

        #加入噪点和噪线
        width = 150
        height = 30

        for i in range(5):      #5条噪线
            x1 = random.randint(0, width)
            x2 = random.randint(0, width)
            y1 = random.randint(0, height)
            y2 = random.randint(0, height)
            draw.line((x1,y1,x2,y2), fill = self.get_random_color())

        for i in range(30):     #30个噪点
            draw.point([random.randint(0, width), random.randint(0, height)], fill = self.get_random_color())
            x = random.randint(0, width)
            y = random.randint(0, height)
            draw.arc((x, y, x + 4, y + 4), 0, 90, fill = self.get_random_color())
            
        img_name_str = [self.get_random_str() for i in range(8)]
        img_name = ''.join(img_name_str)
        img.save(open(img_name + '.png', 'wb'), 'png')

if __name__ == '__main__':
    verify = Gen_Verification_Code()
    num = input('输入要生成的验证码数量：')
    for i in range(int(num)):       #生成一定数量验证码
        verify.gen_veri_code()
