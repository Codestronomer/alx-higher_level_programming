#!/usr/bin/python3
"""
    Filename: 4-from_json_string.py
"""
import json


def from_json_string(my_str):
    """returns the JSON representation of an object"""
    return (json.loads(my_str))
