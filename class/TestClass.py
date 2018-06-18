class Test:
    def  func(self, a):
        pass


class Test1(Test):
    def __init__(self):
        super().__init__()
    
    def func(self):
        pass


c = Test1()
print(c.func('a'))