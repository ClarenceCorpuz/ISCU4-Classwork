from typing import List


def sum_scary_13(numbers: List[int]):
    sum = 0
    i = 0
    while i < len(numbers):
        if numbers[i] != 13:
            sum += numbers[i]
            i += 1
        else:
            i += 2
            
    return sum

