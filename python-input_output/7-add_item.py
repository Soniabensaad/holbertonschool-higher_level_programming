#!/usr/bin/python3
"""
Load, add, save
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    new_file = load_from_json_file("add_item.json")
except FileNotFoundError:
    new_file = []
argc = len(sys.argv)
for i in range(1, argc):
    new_file.append(sys.argv[i])
save_to_json_file(new_file, "add_item.json")
