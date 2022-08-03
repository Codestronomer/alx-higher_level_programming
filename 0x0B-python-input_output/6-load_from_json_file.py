#!/usr/bin/python3
import json
"""
    filename: 6-load_from_json_file.py
"""


def load_from_json_file(filename):
    """creates an object from a 'JSON file'"""
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.loads(f))
