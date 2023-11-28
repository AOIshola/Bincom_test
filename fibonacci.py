#!/bin/python3
"""Sum the first 50 fibonacci sequence"""

def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

first_50 = fibonacci(50)
sum_first_50 = sum(first_50)

print(sum_first_50)