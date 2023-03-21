#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from platform import python_version
import imaplib
import email
import time
from bs4 import BeautifulSoup

 
def send_email():
    server = 'smtp.yandex.ru'
    user = 'ya-lka@yandex.ru'
    password = 'zofzzqmauxwisppe'
     
    recipients = 'mirror@hdrezka.ag'
    sender = 'ya-lka@yandex.ru'
    text = ' '

    msg = MIMEMultipart('alternative')
    msg['From'] = 'Reznik Olga <' + sender + '>'
    msg['To'] = recipients
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'Python/'+(python_version())
     
    part_text = MIMEText(text, 'plain')
     
    msg.attach(part_text)
     
    mail = smtplib.SMTP_SSL(server, 465)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()

send_email()
time.sleep(4)

FROM = 'mirror@hdrezka.org' #'o.reznik@cznanapa.ru'
MYMAIL = 'ya-lka@yandex.ru'
PASSWORD = 'zofzzqmauxwisppe'
IMAPMAIL = 'imap.yandex.ru'


mail = imaplib.IMAP4_SSL(IMAPMAIL)
mail.login(MYMAIL, PASSWORD)
 
mail.list()
mail.select("inbox")

result, data = mail.search(None, f'HEADER FROM {FROM}')
 
ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1]
 
result, data = mail.fetch(latest_email_id, "(RFC822)")
raw_email = data[0][1]
raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)

def multiparting(email_message):
    body = ''
    if email_message.is_multipart():
        for payload in email_message.get_payload():
            body = payload.get_payload(decode=True).decode("UTF-8")
    soup = BeautifulSoup(body, 'html.parser')
    a_tag = soup.find('a', href=True)
    print(a_tag['href'])

multiparting(email_message)
