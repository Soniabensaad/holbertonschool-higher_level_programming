#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence[:1] = None
    tuple = (len(sentence), sentence[:1])
    return (tuple)