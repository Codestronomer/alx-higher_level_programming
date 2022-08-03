#!/usr/bin/python3
"""
    Filename: 0-read_file.py
"""


def read_file(filename=""):
    """reads a text file and prints it to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
