def check_zero_division(func):
    def inner(a, b):
        if b == 0:
            print("Cannot divide by zero")
            return 
        func(a, b)
    return inner

@check_zero_division
def divide(a, b):
    print(a/b)

divide(1, 0)

# func_call = check_zero_division(divide)
# func_call(1, 0)