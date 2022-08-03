#!/usr/bin/python3
"""
    Filename: 7-add_item.py
"""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if __name__ == '__main__':
    f = 'add_item.json'
    cnt = load_from_json_file(f)
    for i in sys.argv[1:]:
        cnt.append(i)
    save_to_json_file(cnt, f)
