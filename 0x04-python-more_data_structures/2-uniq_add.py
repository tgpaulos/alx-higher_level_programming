#!/usr/bin/python3

def uniq_add(my_list=[]):
# Convert the list to a set to remove duplicates
    unique_integers = set(my_list)
# Sum all the unique integers  
    sum_of_integers = sum(unique_integers)
    return sum_of_integers
