#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n rows.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            # Each element is the sum of the two elements directly above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
