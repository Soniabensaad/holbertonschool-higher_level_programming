#!/usr/bin/python3
"""
Write to a file
"""

def write_file(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
        