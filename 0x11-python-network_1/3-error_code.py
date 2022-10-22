#!/usr/bin/python3
"""
script takes ina URL and displays the body of the response
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        try:
            page = response.read()
            print(page.encode("utf-8"))
        except HTTPError as e:
            print("Error code: ", e.code)
