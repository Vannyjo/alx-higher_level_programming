#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        n = len(str) + n
    if n < 0 or n >= len(str):  # If n is out of bounds
        return str
    return str[:n] + str[n+1:]
