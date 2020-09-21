from typing import Dict, List


# Fill in the return statement (2 marks)

    
def give_me_five():
    """This function literally returns the number 5.
    
    Returns:
        The number 5
    
    give_me_five() -> 5
    """
    return 5
    


# Complete the function (2 marks)


def hi_times(n: int) -> str:    
    """Will repeat the string 'hi' n times.
    
    Args:
        n: The number of times to repeat the string "hi".
    Returns:
        A string with 'hi' repeated multiple times.
    
    hi_times(3) -> "hihihi"
    hi_times(5) -> "hihihihihi"
    """    
    return "hi" * n


# Complete the function's parameters (1 mark).
# Complete the function (2 marks)
# Typing is optional.

def greet(name: str):
    """Creates a greeting for a person.
    
    Args:
        name (str): The person to greet.
    Returns:
        (str) A text greeting to the person in the format:
        'It is a pleasure to meet you {person}.'
    """    
    return  f'It is a pleasure to meet you {name}.'
    


# Complete the entire function 
# using the given doc-string. (5 marks)
# The name of the function will be 'below_50'
# Typing is optional.

def below_50(nums: List[int]):
    """Returns only the numbers below 50 from a given list.

    Args:
        numbers (list): A list of integers from 1-100.
    Returns:
        (list) A subset of only the numbers from
        the original list which are below 50.
    
    below_50([5, 50, 55]) -> [5]
    below_50([51, 100, 200]) -> []
    """    
    new_list = []
    for num in nums:
        if num < 50:
            new_list.append(num)
    return new_list
    


# Complete the entire function
# using the given doc-string. (5 marks)
# The name of the function will be 'get_stock'

def get_stock(item, inventory):
    """Search for an item's stock level in a store's inventory.
    
    The inventory is a dictionary of items (key) and quantity (value).
    If the item does not appear in the store's inventory at all
    return a value of -1.

    Args:
        item (str): The item to look for.
        inventory (Dict[str, int]): The store's inventory
            with a key: value mapping of item(str): quantity(int).
            
            e.g., "apples": 55  
            # The store sells apples and has 55 in stock.
        
    Returns:
        (int) The quantity of the requested item. Return -1 if
        the item does not appear in the inventory at all.
    
        Given the following inventory dict:
        inventory = {
            "apples": 3,
            "oranges": 0
        }

        get_stock("apples", inventory) -> 3
        get_stock("oranges", inventory) -> 0
        get_stock("crossbow", inventory) -> -1
    """
    if item not in inventory.keys():
        return -1
    else:
        return inventory[item]
