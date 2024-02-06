#!/usr/bin/python3

"""Reading a text file"""


def read_file(filename=""):

    """A functions that reads a text file and prints it to stdout

    Args:
        filename (str): The name of the file to read from.

    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
