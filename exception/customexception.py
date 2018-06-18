# Custom exception class
class MyCustomException(Exception):
    # pass
    def __init__(self, message, errors):
        super().__init__(message)
        self.message = message
        self.errors = errors

    def __str__(self):
        return self.message
try:
    raise MyCustomException("This is a custom exception", {'hey': 'hey'})

except MyCustomException as e:
    print(e.message)
    # print("Hey! we raised an exception")


