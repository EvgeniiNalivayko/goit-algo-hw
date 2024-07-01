import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:

    if min < 1 or  max > 1000:
        raise ValueError("Min val >= 1")
 
    if quantity > (max-min + 1 ) :
    
       raise ValueError('More then max')
 
    numbers = random.sample(range(min, max + 1), quantity)
   
    numbers.sort()
    
    return numbers

