#!/usr/bin/python3

# A python Password generator
# Developed by Elieroc
# Start of project : 19/10/2020
# Actual version : 1.1

from random import *

dictionary=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "&", "~", "é", "#", "{", "[", "(", "-", "|", "`", "è", "_", "ç", "^", "@", ")", "]", "}", "+", "*", ".", "!", "!", ":", ";", "§"]

def generator(lengt=32):
    password = str()
    for i in range(lengt):
        rand_len = randint(0, len(dictionary)-1)
        password += dictionary[rand_len]
    return password
