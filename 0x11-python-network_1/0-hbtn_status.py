#!/usr/bin/python3
"""
A python script that fetchs 'https://alx-intranet.hbtn.io/status'
"""
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        page = response.read()
        print("Body response:")
        print(f"\t- type: {type(page)}")
        print(f"\t- content: {page}")
        print(f"\t- utf8 content: {page.decode(encoding='utf-8')}")
