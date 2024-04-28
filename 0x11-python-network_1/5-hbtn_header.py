#!/usr/bin/python3

"""
a Python script that takes in a URL, sends a request to the URL 
and displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys

url = sys.argv[1] 
response = requests.get(url)
request_id = response.headers.get('X-Request-Id')

if request_id:
    print(request_id)
else:
    print('X-Request-Id not found in the response header')
