# Generate virtually infinite pool of integers
def sample_generator():
    x = 0
    while True:
        yield x + 1
        x += 1

# my_generator = sample_generator()
