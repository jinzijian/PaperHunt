import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

def send_email(report):
    # 从环境变量中获取邮箱信息
    email_user = os.getenv('EMAIL_USER')
    email_password = os.getenv('EMAIL_PASSWORD')
    email_host = os.getenv('EMAIL_HOST')
    email_port = int(os.getenv('EMAIL_PORT'))
    to_email = os.getenv('TO_EMAIL')

    msg = MIMEText(report, 'plain', 'utf-8')
    msg['Subject'] = '每日论文汇总'
    msg['From'] = email_user
    msg['To'] = to_email

    try:
        # 连接到 Gmail SMTP 服务器，使用 SSL 加密
        server = smtplib.SMTP_SSL(email_host, email_port)
        server.login(email_user, email_password)
        server.send_message(msg)
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print(f"邮件发送失败：{e}")

if __name__ == '__main__':
    # 定义测试报告内容和收件人邮箱
    test_report = '这是一封测试邮件，来自于 send_email 函数的测试。'

    # 调用 send_email 函数
    send_email(test_report)
