#!/usr/bin/python3
"""This module defines the divides of all elements in a matrix function
"""
def matrix_divided(matrix, div):
    """ Function that div all element of matrix.
    Args:
        matrix (int, float): Matrix to divide
    Returns:
        list: New matrix
    """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        for i in row:
            if (type(i) != int and type(i) != float) or i != i:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div != div or div == float('inf'):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    a = len(matrix[0])
    for i in matrix:
        if a != len(i):
            raise TypeError ("Each row of the matrix must have the same size")
    N_matrix = []
    for i in matrix:
        N_list =[]
        for j in i:
            N_list.append(round(j/div, 2))
        N_matrix.append(N_list)
    return N_matrix
