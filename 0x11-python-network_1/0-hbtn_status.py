#!/usr/bin/python3
"""
A python script that fetchs 'https://alx-intranet.hbtn.io/status'
"""
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        print(dir(response))
        print(response.read())
