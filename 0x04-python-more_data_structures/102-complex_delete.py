#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    # Create a list to store keys to be deleted
    keys_to_delete = []

    # Iterate over each key-value pair in a_dictionary
    for k, v in a_dictionary.items():
        if v == value:
            keys_to_delete.append(k)

    # Delete the keys from a_dictionary
    for k in keys_to_delete:
        del a_dictionary[k]

    return a_dictionary
