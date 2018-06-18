"""
Example of nested function
"""

def outer_func():
    outer_func_var = 1

    def inner():
        inner_func_var = 2
        print(inner_func_var)
    
    return inner


# driver block 
def main():
    func_obj = outer_func()
    func_obj()

main()