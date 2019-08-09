# -- coding: utf-8 --
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class email:
      def send_email(self):
        # ----------1.跟发件相关的参数------
        smtpserver = "smtp.163.com"  # 发件服务器
        port = "0"  # 端口
        sender = "15712090680@163.com"  # 账号
        psw = "123456a"  # 密码
        receiver = ["tanjiahua@tekuaikeji.com","15712090680@163.com"]  # 接收人

        # 读文件
        file_path = "C:\\Users\\hx\\PycharmProjects\\interfacefk\\test_report\\result.html"
        with open(file_path, "rb") as fp:
            mail_body = fp.read()
        msg = MIMEMultipart()
        msg["from"] = sender  # 发件人
        msg["to"] = ";".join(receiver)  # 收件人
        msg["subject"] = "风控自动化测试"  # 主题

        # 正文
        body = MIMEText(mail_body, "html", "utf-8")
        msg.attach(body)

        # 附件
        att = MIMEText(mail_body, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="test_report.html"'
        msg.attach(att)
        # ----------3.发送邮件------
        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)  # 连服务器
            smtp.login(sender, psw)
        except:
            smtp = smtplib.SMTP_SSL(smtpserver, port)
            smtp.login(sender, psw)  # 登录
        smtp.sendmail(sender, receiver, msg.as_string())  # 发送
        smtp.quit()
if __name__ == '__main__':
       email = email()
       email.send_email()