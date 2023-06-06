#!/usr/bin/python3
import urllib.request
import sys
"""Python script that takes in a URL, sends a request to the URL and displays 
the value of the X-Request-Id variable found in the header
"""
url = sys.argv[1]

"""Send a GET request to the URL"""
with urllib.request.urlopen(url) as response:
    """Get the value of the X-Request-Id header"""
    x_request_id = response.getheader('X-Request-Id')

    """Display the value of the X-Request-Id variable"""
    print(x_request_id)
