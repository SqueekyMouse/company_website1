import os
import smtplib,ssl

def send_email(msg):
    host='smtp.gmail.com'
    port=465

    username='appuser565@gmail.com'
    password=os.getenv('APP_M_PASSWORD')

    receiver='appuser565@gmail.com'
    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host,port=port,context=context) as server:
        server.login(user=username,password=password)
        server.sendmail(from_addr=username,to_addrs=receiver,msg=msg)

if __name__=='__main__':
    msg="""Subject: New Inquiry\nType:Job Inquiries\nHi\nemail: a@b.com"""
    send_email(msg)