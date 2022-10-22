#!/usr/bin/python3
"""
A python script that takes in a URL, and displays the value of the
X-Request-id variable found in the header of the response
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        page = response.info()
        print(page['X-Request-Id'])
