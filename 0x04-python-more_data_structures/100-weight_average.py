#!/usr/bin/python3

def weight_average(my_list=[]):
    # Check if the list is empty
    if len(my_list) == 0:
        return 0
    
    # Initialize variables to store the sum of products and sum of weights
    sum_products = 0
    sum_weights = 0
    
    # Iterate over each tuple in my_list
    for score, weight in my_list:
        # Calculate the product of score and weight and add it to sum_products
        sum_products += score * weight
        # Add the weight to sum_weights
        sum_weights += weight
    
    # Calculate the weighted average
    weighted_average = sum_products / sum_weights
    
    return weighted_average
