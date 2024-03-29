#!/usr/bin/python3
"""
    filename: 5-save_to_json_file.py
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON Representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (json.dump(my_obj, f))
