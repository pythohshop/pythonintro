class Stack:
    def __init__(self, datas):
        self.data = []
        for data in datas:
            self.push(data)

    def is_empty(self):
        return self.data == []
    
    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return 
        else:
            return self.data.pop()
    
    def push(self, data):
        self.data.append(data)
    
    def peek(self):
        return self.data[len(self.data) -1]
    
    def get_stack(self):
        return self.data

    def __str__(self):
        return str(self.data)