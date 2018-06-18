# Fibonacci generator
def fib_generator():
    a, b = 0, 1

    while True:
        yield a 
        a, b = b, a + b

# Driver program 
def main():
    fib_gen = fib_generator()
    for i in range(10):
        print(next(fib_gen))

main()
