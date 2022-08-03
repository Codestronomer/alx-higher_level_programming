#!/usr/bin/python3
import json
"""
    filename: 5-save_to_json_file.py
"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON Representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
