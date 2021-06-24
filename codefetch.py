#coding: utf-8
from imap_tools import MailBox
import re

# This will look for a 6 digit numeric code in the most recent (and unseen) mail message, specifically in the subject 
def verification():
        with MailBox('imap.gmail.com').login('user', 'password', 'INBOX') as mailbox:
            criteria = 'UNSEEN'
            for msg in mailbox.fetch(criteria, bulk=True, limit=1):
                        s = msg.subject
                        text = re.findall(r"(?<!\d)\d{6}(?!\d)", s)
                        return text