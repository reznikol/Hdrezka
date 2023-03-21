#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from platform import python_version
import datetime as dt
import time
 
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
