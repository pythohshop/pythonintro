class Base:
    def __init__(self, a):
        self.a = a
    


class Child(Base):
    def __init__(self, a):
        super().__init__(a)
    

c = Child('a')