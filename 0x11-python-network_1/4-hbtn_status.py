#!/usr/bin/python3

"""a Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests

respo = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(respo.text)))
print("\t- content: {}".format(respo.content))
print("\t- utf8 content: {}".format(respo.text))
