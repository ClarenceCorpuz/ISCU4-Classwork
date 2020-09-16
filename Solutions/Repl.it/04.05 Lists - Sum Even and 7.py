04.05 Lists - Sum Even and 7

def sum_even_and_7(numbers: List[int]):
    sum = 0
    for num in numbers:
        if num % 2 == 0 or num == 7:
            sum += num
    return sum
