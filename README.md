nexus6-check
============

This is a little script that polls the nexus6 release site.
Once a change occurs on the site (indicating that the device is available), an email will be sent as a notification.

Run it as a cron job!

In order to make the script work, a "data.json" file in the following format has to be added to the project root.

    {
      "recipients": ["test@test.net"],
      "sender": "nexus6-check@mydomain.de",
      "positive_body": "check http://www.google.com/nexus/6",
      "negative_body": "",
      "positive_subject": "NEXUS6 MIGHT BE AVAILABLE!!!",
      "negative_subject": "nexus6 is still not available..."
    }
