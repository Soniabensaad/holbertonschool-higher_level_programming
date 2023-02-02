#!/usr/bin/python3
"""
prints a text with 2 new lines
after each of these characters: ., ? and :
"""

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new = ""
    for char in text:
        new += char
        if char in ["?", ".", ":"]:
            new += "\n\n"
    print(new)
    