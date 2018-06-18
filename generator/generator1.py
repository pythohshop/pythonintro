def function():
     yield 1


a = function()
print(next(a))