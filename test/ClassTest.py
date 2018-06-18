class Parent:
    def __init__(self, a, b):
        print("This is Parent")

class Parent1:
    def __init__(self):
        print("This is parent 1")
    

class Child(Parent, Parent1):
    def __init__(self):
        print("This is child")
        Parent.__init__(self, 'h', 'b')
        Parent1.__init__(self)


c = Child()
