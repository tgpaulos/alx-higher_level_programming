#!/usr/bin/python3
"""
 a Python script that takes in a URL, sends a request to the URL 
 and displays the body of the response (decoded in utf-8).
"""

import sys
from urllib import request, error


url = sys.argv[1]

try:

    with request.urlopen(url) as response:

        response_body = response.read().decode('utf-8')
        print(response_body)
except error.HTTPError as e:

    print(f"Error code: {e.code}")
