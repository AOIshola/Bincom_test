#!/bin/python3
"""generates a binary digit of 4 digits"""

import random

def generate_bits():
    """generates 4-digit bits"""
    string = ""
    for i in range(4):
        bit = random.randint(0, 1)
        string += str(bit)
    print(f"Randomly generated string is {string}")
    return string

string = generate_bits()


def binary_to_uint(string):
    """converts binary value to decimal"""
    base_10 = 0
    exp = 1
    for char in string[::-1]:
        if char == '0':
            exp *= 2
        elif char == '1':
            base_10 += exp
            exp *= 2
    print(f"{string} converted to base_10 is {base_10}")

binary_to_uint(string)