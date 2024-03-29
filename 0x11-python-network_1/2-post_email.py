#!/usr/bin/python3
"""
Python script takes in a URL and an email, sends a POST request
to the passed URL with the email as a paramenter, and displays the
body of the response
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page.decode(encoding="utf-8"))
