#!/usr/bin/python3
"""
    filename: 12-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the pascal's triangle
    """
    p_triangle = []
    if n <= 0:
        return p_triangle
    p_triange = [[1]]
    for i in range(1, n):
        sub_l = [1]
        prev_l = p_triangle[i - 1]
        for j in range(1, prev_l):
            sub_l.append(prev_l[j] + prev_l[j - 1])
        sub_l.append(1)
        triangle.append(row)
    return (triangle)
