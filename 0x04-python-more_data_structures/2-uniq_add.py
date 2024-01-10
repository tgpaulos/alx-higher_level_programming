#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_integers = set(my_list)  # Convert the list to a set to remove duplicates
    sum_of_integers = sum(unique_integers)  # Sum all the unique integers
    return sum_of_integers
