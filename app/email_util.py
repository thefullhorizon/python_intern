# -*- coding=utf-8 -*-
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from project.io_util import read_dict

"""

集成通用的发邮件工具类
参考学习：https://blog.csdn.net/qq_38700592/article/details/105914464

Author       :   Cucumber
Date         :   10/20/20

"""


class QQClient:

    host = 'smtp.qq.com'
    port = 465
    user = '3157398745@qq.com'
    sender = user
    from_alias = 'Cucumber Data Institute'

    def __init__(self, receivers):
        self.receivers = receivers
        self.qq_password = self.obtain_password()

    def obtain_password(self):
        config_path = '/Users/nashan/Documents/WS/pycharm/python_learning/security_center.config'
        dict_obj = read_dict(config_path)
        return dict_obj['qq_password']

    def try_send(self, message):
        try:
            message['From'] = self.from_alias
            message['To'] = self.receivers[0]
            qq_client = smtplib.SMTP_SSL(self.host, port=self.port)
            qq_client.login(user=self.user, password=self.qq_password)
            qq_client.sendmail(from_addr=self.sender, to_addrs=self.receivers, msg=message.as_string())
            print("Sent email successfully")
            qq_client.quit()
        except smtplib.SMTPException as e:
            print("Sent email failed: {}".format(e))

    def text_plain(self, email_title, email_content):
        message = MIMEText(_text=email_content, _subtype='plain', _charset='utf-8')
        message['Subject'] = email_title
        self.try_send(message)

    def text_with_attachment(self, email_title, email_content, attachment_path, attachment_name):
        """
        以附近的形式发送邮件
        :param email_title:
        :param email_content:
        :param attachment_path: r'/Users/nashan/.../data_analysis.png'
        :param attachment_name: data_analysis.png
        """
        message = MIMEMultipart()
        message['Subject'] = email_title
        message.attach(MIMEText(email_content, 'html', 'utf-8'))
        if attachment_path is not None:
            with open(attachment_path, 'rb') as fp:
                attachment_obj = MIMEText(fp.read(), 'base64', 'utf-8')
            attachment_obj["Content-Type"] = 'application/octet-stream'
            attachment_obj["Content-Disposition"] = 'attachment; filename="{}"'.format(attachment_name)
            message.attach(payload=attachment_obj)

        self.try_send(message)

    def text_with_image(self, email_title, email_content, accessory_pic=None):
        """
        以图文的方式发送邮件,一个方法相当于定义了一套邮件模板
        :param email_title:
        :param email_content:
        :param accessory_pic:
        """
        message = MIMEMultipart(_subtype='related')
        message['Subject'] = email_title

        email_content_template = """
            <p>{}</p>
            <p><img src='cid:image_id'></p>
            <p>{}</p>
            """.format(email_content, self.get_email_sign())

        msgAlternative = MIMEMultipart('alternative')
        msgAlternative.attach(MIMEText(email_content_template, 'html', 'utf-8'))
        message.attach(msgAlternative)

        with open(accessory_pic, 'rb') as fp:
            msgImage = MIMEImage(fp.read())
        msgImage.add_header(_name='Content-ID', _value='<image_id>')
        message.attach(msgImage)

        self.try_send(message)

    @staticmethod
    def get_email_sign():
        return """
        For more information 
        <br> Please contact 3157398745 | shanghai
        """
