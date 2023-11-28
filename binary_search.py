#!/bin/python3
"""This program implements a recursive searching algorithm
with the binary search method"""

def binary_search(my_list, searchKey, low, high):
    """Finds a number entered by a user"""
    if not my_list:
        return -1
    mid = (low + high) // 2

    while low <= high:
        if searchKey == my_list[mid]:
            return mid
        elif searchKey < my_list[mid]:
            return binary_search(my_list, searchKey, low, mid - 1)
        elif searchKey > my_list[mid]:
            return binary_search(my_list, searchKey, mid + 1, high)
    return -1

key = int(input("Search for: "))
my_list = [1, 2, 3, 4, 5, 6, 7]
pos = binary_search(my_list, key, 0, len(my_list) - 1)
print(pos)