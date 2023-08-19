#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row_i in matrix:
        for col in row_i:
            if col == row_i[-1]:
                print('{:d}'.format(col), end='')
            else:
                print('{:d}'.format(col), end=' ')
        print()
