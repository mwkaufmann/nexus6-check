#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Mario Kaufmann'

from send_mail import send_notifications
import urllib.request
import json


if __name__ == "__main__":

    url = "http://www.google.de/nexus/6"
    data = json.load(open("data.json", "r"))

    google_response = urllib.request.urlopen(url)
    html = google_response.read().decode(encoding='UTF-8')

    site_has_changed = not ("Available for pre-order starting in late October.") in html

    if site_has_changed:
        send_notifications(data.recipients, data.sender, data.positive_subject, data.positive_message)

    else:
        send_notifications(data.recipients, data.sender, data.negative_subject, data.negative_message)
