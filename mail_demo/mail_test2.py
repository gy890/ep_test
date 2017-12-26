# coding=utf-8
"""
Created on 2017-12-26

@Filename: mail_test2
@Author: Gui


"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'ee890119a@163.com'  # 邮件发送人
receiver = '878248393@qq.com'  # 邮件收件人
subject = 'python email test...'  # 主题
smtpserver = 'smtp.163.com'  # 网易的STMP地址 默认端口号为25
username = 'ee890119a@163.com'  # 发送邮件的人
password = 'AA1EE4CC7ac'  # 你所设置的密码.网易在开通SMTP服务后会有个密码设置

# 中文需参数‘utf-8'，单字节字符不需要
msg = MIMEText('This is a test email ... you can delete it ', 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')  # 头部信息:标题
msg['From'] = 'Tim<ee890119a@163.com>'  # 头部信息:名称<发件人的地址>
msg['To'] = "878248393@qq.com"  # 头部信息:收件人地址
try:
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')  # 链接服务器
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('success')
except smtplib.SMTPException:
    print('Error: fail')