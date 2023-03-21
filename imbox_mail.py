#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
 
 
import imaplib
import email
from bs4 import BeautifulSoup


FROM = 'mirror@hdrezka.org'
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
