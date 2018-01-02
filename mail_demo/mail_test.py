# coding=utf-8
"""
Created on 2017-12-26

@Filename: mail_test
@Author: Gui


"""
import logging
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.image import MIMEImage

sender = 'ee890119a@163.com'
to = ['878248393@qq.com', 'gui.yun@e-ports.com']
cc = ['2670042680@qq.com', 'ee890119a@163.com']
bcc = ['yawn1122@aliyun.com', ]
receiver = to + cc + bcc
subject = 'python email'
smtpserver = 'smtp.163.com'
username = 'ee890119a@163.com'
password = 'AA1EE4CC7ac'

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'Tim<ee890119a@163.com>'  # 头部信息:名称<发件人的地址>
msg['To'] = ','.join(to)  # 头部信息:收件人地址
msg['Cc'] = ','.join(cc)
msg['Bcc'] = ','.join(bcc)

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """
<html> 
  <head></head> 
  <body> 
    <p>Hi!<br> 
       How are you?<br> 
       Here is the <a href="http://www.python.org">link</a> you wanted. <br>
       中文测试
    </p> 
  </body> 
</html> 
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# 构造附件
att1 = MIMEText(open('mail_test.py', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="mail_test.py"'
msg.attach(att1)
att2 = MIMEText(open('a.jpg', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="a.jpg"'
msg.attach(att2)
att3 = MIMEText(open('壁纸.jpg', 'rb').read(), 'base64', 'utf-8')
att3["Content-Type"] = 'application/octet-stream'
# att3["Content-Disposition"] = 'attachment; filename="{}"'.format('壁纸.jpg'.encode('utf-8'))
att3.add_header('Content-Disposition', 'attachment', filename=('gbk', '', '壁纸.jpg'))
# encoders.encode_base64(att)
msg.attach(att3)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # filename='test.log',
                    # filemode='w',
                    )
try:
    smtp = smtplib.SMTP()
    smtp.set_debuglevel(1)
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    logging.info('success')
except smtplib.SMTPException as e:
    logging.warning('Error: fail', e)
