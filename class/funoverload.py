class FunAdd:
    def __init__(self, data):
        self.data = data
    
    def __add__(self, other):
        print('self: ', self)
        print('other: ', other)
        return str(self.data) + str(other.data)
       

num1 = FunAdd(1)
num2 = FunAdd(2)

print(num1 + num2)