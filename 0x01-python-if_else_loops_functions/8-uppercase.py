#!/usr/bin/python3
def uppercase(string):
    uppercase_str = ""
    for char in string:
        uppercase_char = chr(ord(char) - 32) if ord(char) >= 97 and ord(char) <= 122 else char
        uppercase_str += uppercase_char
    
    print(uppercase_str)
