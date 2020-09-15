
01.01 Intro: f(x) = x + 4

def f(x: int):
    x = x + 4
    return x


    """ Or
    
    return x + 4
    """

01.02 Intro: say_hello

def say_hello(name: str):
    greeting = f"Hello, {name}!"
    return greeting


01.03 Intro: Sum of three numbers

def add(a: int, b: int, c: int):
    sum = a + b + c
    return sum


04.01 Lists - Empty List

def get_empty_list():
    emptylist = []
    return emptylist 


04.02 Lists - Pi List


04.03 Lists - Sum

def sum_list(numbers: List[float]) -> float:
    sum = 0.0
    for num in numbers:
        sum += num
    return sum


04.04 Lists - Sum Even

def sum_even(numbers: List[int]):
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    return sum


04.05 Lists - Sum Even and 7

def sum_even_and_7(numbers: List[int]):
    sum = 0
    for num in numbers:
        if num % 2 == 0 or num == 7:
            sum += num
    return sum

