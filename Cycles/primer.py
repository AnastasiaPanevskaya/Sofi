def is_rhomb(a_size: float, b_size: float) -> bool:
    return a_size == b_size 

def print_hi(name: str = 'stranger') -> None:
    print('Hi,' + name + '!')

print(is_rhomb.__annotations__)
print(print_hi.__annotations__)