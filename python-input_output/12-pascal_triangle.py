#!/usr/bin/python3
"""function representing the Pascal’s triangle """


def pascal_triangle(n):
    """return list of lists of integers representing the Pascal triangle """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        cur_row = [1]
        prev_row = triangle[i - 1]
        for j in range(1, i):
            cur_row.append(prev_row[j-1] + prev_row[j])
        cur_row.append(1)
        triangle.append(cur_row)
    return triangle
