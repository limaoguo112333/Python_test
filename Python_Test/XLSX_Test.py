# -*- coding: gbk -*-
#第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示： 请将上述内容写到 student.xls 文件中，如下图所示：
'''
{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
'''
#第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示： 请将上述内容写到 city.xls 文件中，如下图所示：
'''
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
'''
#第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示： 请将上述内容写到 numbers.xls 文件中，如下图所示：
'''
[
	[1, 82, 65535], 
	[20, 90, 13],
	[26, 809, 1024]
]
'''

import json
import re
import xlwt

def get_text(path):
	with open(path, 'r', encoding='utf-8') as f:
		text = f.read()
		print(text)
		text_json = json.loads(text)	#json格式加载文件
	return text_json

def save_excel_1(content_dict, excel_name):
	wb = xlwt.Workbook()	#创建工作本

	ws = wb.add_sheet(excel_name, cell_overwrite_ok = True)
	row = 0

	for k, v in sorted(content_dict.items(), key = lambda d:d[0]):
		col = 0
		ws.write(row, col, k)
		for item in v:
			col += 1
			ws.write(row, col, item)

		row += 1

	wb.save(excel_name + '.xls')

def save_excel_2(content_dict, excel_name):
	wb = xlwt.Workbook()

	ws = wb.add_sheet(excel_name, cell_overwrite_ok = True)
	row = 0

	for k, v in sorted(content_dict.items(), key = lambda d:d[0]):
		col = 0
		ws.write(row, col, k)
		col += 1
		ws.write(row, col, v)

		row += 1

	wb.save(excel_name + '.xls')

def save_excel_3(content_dict, excel_name):
	wb = xlwt.Workbook()

	ws = wb.add_sheet(excel_name, cell_overwrite_ok = True)
	row = 0

	for k in content_dict:
		col = 0
		for item in k:
			ws.write(row, col, item)
			col += 1

		row += 1

	wb.save(excel_name + '.xls')

if __name__ == '__main__':
	text_name_1 = 'student.txt'
	save_excel_1(get_text(text_name_1), text_name_1.split('.')[0])
	text_name_2 = 'city.txt'
	save_excel_2(get_text(text_name_2), text_name_2.split('.')[0])
	text_name_3 = 'numbers.txt'
	save_excel_3(get_text(text_name_3), text_name_3.split('.')[0])
