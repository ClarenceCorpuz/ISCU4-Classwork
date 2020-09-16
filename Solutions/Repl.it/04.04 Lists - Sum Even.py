04.04 Lists - Sum Even

def sum_even(numbers: List[int]):
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    return sum


