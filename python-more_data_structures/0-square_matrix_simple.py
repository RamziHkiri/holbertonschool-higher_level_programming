#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        row_squar = [element ** 2 for element in row]
        new_matrix.append(row_squar)
    return new_matrix
