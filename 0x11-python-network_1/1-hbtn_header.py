#!/usr/bin/python3

import urllib.request
import sys

"""
a Python script that takes in a URL, sends a request to the URL and displays 
the value of the X-Request-Id variable found in the header of the response.
"""

# Take the URL from the command line argument
url = sys.argv[1]

# Send a request to the URL
with urllib.request.urlopen(url) as response:
    
    headers = response.info()
    
    x_request_id = headers.get('X-Request-Id')
    
    print(x_request_id)
