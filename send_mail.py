#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Mario Kaufmann'

import smtplib
from email.mime.text import MIMEText


def send_notifications(recipients, sender, msg, subject):

    msg = MIMEText(msg)

    for recipient in recipients:
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient

        s = smtplib.SMTP('localhost')
        s.sendmail(sender, [recipient], msg.as_string())
        s.quit()


