"""
pasing function as a argument to another function 
and returning a function 
"""

def func():
    print("Hello this is the function to be passed back and forth")

def returner(func):
    return func

def caller():
    func_obj = returner(func)
    func_obj()

caller()