# There is no method overloading in python 
# Cannot have more than one method with the same name

# Demo 

class Overloading:
#     def method(self, message):
#         print(message)
    
#     def method(self, message, error):
#         print(message)
#         print(error)
    
    def method(self, message, *args, **kwargs):
        print(message)
        print(args)
        print(kwargs)

over = Overloading()
over.method("This is the passed method", 'a', 'b', c='c', d='d')