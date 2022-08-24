# -*- coding: gbk -*-
# 过滤邮箱中未读邮件，并对特定格式主题的邮件作出回复

from smtplib import SMTP
import email
from email.header import Header
from email.mime.text import MIMEText
import imaplib
import re
from threading import Thread
from time import sleep
import pandas as pd

class Mail:
    isrun = True

    def __init__(self):
        self.user_id = 'xxxx@163.com'
        self.password = 'XXXXXXXXXXXX'  #163邮箱授权码
        self.imap_server = 'imap.163.com'
        self.smtp_server = 'smtp.163.com'

    def imap_login(self):
        try:
            imaper = imaplib.IMAP4_SSL(self.imap_server, 993)   #连接IMAP服务器
            print('IMAP4服务器连接成功')
        except Exception as e:
            print('IMAP4服务器连接失败：', e)
                
        try:
            imaper.login(self.user_id, self.password)   #登录邮箱
            print('IMAP4登录成功')
            imaplib.Commands['ID'] = 'AUTH'     #上传客户端身份信息（仅163、126邮箱）
            args = ("name", "xxxx", "contact", "xxxx@163.com", "version", "6.0.0", "vendor", "myclient")
            typ, dat = imaper.xatom('ID', '("' + '" "'.join(args) + '")')
            return imaper
        except Exception as e:
            print('IMAP4登录失败：', e)

    def receive_email(self, imaper):
        state, number = imaper.select('INBOX')  #163邮箱select前要上传客户端信息，否则报错
        code, id_list = imaper.search(None, 'UNSEEN')   #过滤未读邮件，获取全部邮件用'ALL'
        email_list = id_list[0].split()

        if len(email_list) == 0:
            print('未找到未读邮件')
            return

        file = pd.read_excel('C:\\Users\\admin\\Desktop\\info.xlsx', header = None)   #打开需要查询的表格，这里header=None是防止pd自动将表格第一行当作列名
        height, width = file.shape

        for i in range(0, len(email_list)):
            l = len(email_list)
            item = email_list[l - i - 1]   #获取邮件序号
            ret, data = imaper.fetch(item, '(RFC822)')  #获取邮件内容
            msg = email.message_from_string(data[0][1].decode('gbk'))
            #print(msg)
            sub = email.header.decode_header(msg.get('subject'))
            email_from = email.header.decode_header(msg.get('from'))
            textpat = re.compile(r'(\w+)/(\w+)$') #设置邮件主题正则表达式格式，并便于分group
            sub_text = str(email.header.make_header(sub))
            email_from_text = str(email.header.make_header(email_from))
            m = textpat.match(sub_text)
            #print(m)
            if m:
                score = None
                for i in range(height):     #遍历表格每一行，判断是否找到要查询对象
                    row = file.iloc[i].values
                    if str(row[0]) == m.group(2):
                        score = row[1]
                if score == None:
                    print('未找到对象：', m.group(2), 'from', email_from_text)
                    continue
                self.send_email(email_from_text, score)

    def send_email(self, receiver, score):
        msg_text = '已收到, 成绩为：' + str(score)
        message = MIMEText(msg_text, 'plain', 'utf-8')
        message['From'] = self.user_id
        message['To'] = receiver
        message['Subject'] = Header('自动回复', 'utf-8')
        smtper = SMTP(self.smtp_server)
        smtper.login(self.user_id, self.password)
        smtper.sendmail(self.user_id, receiver, message.as_string())
        print('已回复：', receiver)

    def imap_loginout(self, imaper):
        imaper.close
        imaper.logout()
        print('IMAP4已断开连接')

def wait_input():
    while True:
        if input() == 'exit':
            Mail.isrun = False
            break
        else:
            continue

if __name__ == '__main__':
    mail = Mail()
    IMAPER = mail.imap_login()
    t1 = Thread(target = wait_input)
    t1.start()
    while mail.isrun: #10s检查一次未读邮件
        mail.receive_email(IMAPER)
        sleep(10)
    mail.imap_loginout(IMAPER)

