"""
Example of calling function with arguments
"""

# Function definition
def function(apple, ball, cat):
    print('appple: ', apple)
    print('ball: ', ball)
    print('cat: ', cat)

    # Returning something
    return "I can return anything and you don't need to worry about int string float list etc"


# Function call
returned = function(apple= 10, ball = 10, cat = 'black')
print(returned)