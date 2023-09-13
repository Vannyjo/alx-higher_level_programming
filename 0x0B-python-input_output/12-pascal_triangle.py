#!/usr/bin/python3
"""This module defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n
    """
    if n <= 0:
        return []

    triangleNumber = [[1]]
    while len(trianglesNumber) != n:
        triangle = triangles[-1]
        count = [1]
        for i in range(len(tri) - 1):
            count.append(triangle[i] + triangle[i + 1])
        count.append(1)
        triangleNumber.append(tmp)
    return triangleNumber
