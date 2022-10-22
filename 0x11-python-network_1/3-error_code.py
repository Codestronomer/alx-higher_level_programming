#!/usr/bin/python3
"""
script takes ina URL and displays the body of the response
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            page = response.read().decode(encoding="utf-8")
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
