#!/usr/bin/python3
def print_alphabet(letter='A'):
    print(letter, end='')
    if letter != 'Z':
        print_alphabet(chr(ord(letter) + 1))
    else:
        print('\n')

print_alphabet()
