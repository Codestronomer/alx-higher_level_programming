#!/usr/bin/python3
"""
    filename: 1-write_file.py
"""


def write_file(filename="", text=""):
    """writes a string to a text file and return character length"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
