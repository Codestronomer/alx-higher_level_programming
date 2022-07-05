#!/usr/bin/python3
# prints a matrix of integers
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end='')
            if i < (len(row) - 1):
                print(" ", end='')
        print()
