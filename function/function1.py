"""
calling function from one to another to another to ....pass
"""

def apple():
    print("This is a appel function")
    print("Calling function ball")
    print()
    ball()


def ball():
    print("This is a ball function")
    print("Calling function cat")
    print()
    cat()

def cat():
    print("This is a cat function")
    print("Oops! I don't get to call another function")
    print()

apple()
