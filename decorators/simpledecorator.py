def printer():
    print("Hello I am a printer")


def decorator(func):
    def inner():
        # print(type(func))
        print("Hello I need to print first")
        func()
    return inner


caller = decorator(printer)
caller()