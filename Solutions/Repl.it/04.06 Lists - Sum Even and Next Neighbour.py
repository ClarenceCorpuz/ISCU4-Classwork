from typing import List

def sum_even_and_next_neighbour(numbers: List[int]):
    sum = 0
    i = 0 
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            sum += numbers[i]
            sum += numbers[i+1]
            i += 2
        else:
            i += 1
    return sum
    
