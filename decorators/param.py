def decorator(func):
    def inner(a, b):
        func(a, b)
    
    return inner


@decorator
def func(a, b):
    print(a)
    print(b)

func(1, 2)