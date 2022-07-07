#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # computes the square values of all integers of matrix
    new_matrix = [[i*i for i in row] for row in matrix]
    return new_matrix
