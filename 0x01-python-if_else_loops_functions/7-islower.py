#!/usr/bin/python3
# Author - isaiahKC
def islower(c):
    '''checks for lowercase character.'''
    alphabet = []
    start = ord('a')
    for i in range(26):
        alphabet.append(chr(start + i))
    return(c in alphabet)
