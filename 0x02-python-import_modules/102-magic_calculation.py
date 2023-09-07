from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    add_result = add(a, b)
    
    for i in range(4, 6):
        add_result = add(add_result, i)

    if a < b:
        return add_result
    else:
        return sub(a, b)
