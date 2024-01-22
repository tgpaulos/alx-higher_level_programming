#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result = []
    
    # Iterate over each row in the input matrix
    for row in matrix:
        new_row = []
        
        # Iterate over each element in the row and compute the square value
        for num in row:
            new_row.append(num ** 2)
        
        # Add the new row to the result matrix
        result.append(new_row)
    
    # Return the new matrix with squared values
    return result
