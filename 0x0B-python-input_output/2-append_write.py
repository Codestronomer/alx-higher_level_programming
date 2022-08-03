#!/usr/bin/python3
"""
    filename: 2-append_write.py
"""


def append_write(filename="", text=""):
    """writes a string to a text file and return character length"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
