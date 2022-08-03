#!/usr/bin/python3
"""
    filename: 6-load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """creates an object from a 'JSON file'"""
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.loads(f))
