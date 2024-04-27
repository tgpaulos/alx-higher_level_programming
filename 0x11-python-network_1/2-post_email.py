#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""

import sys
from urllib import parse, request

url = sys.argv[1]
email = sys.argv[2]

data = parse.urlencode({'email': email}).encode()

req = request.Request(url, data=data)

with request.urlopen(req) as response:
    response_body = response.read().decode('utf-8')
    print(response_body)
