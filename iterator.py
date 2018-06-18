string = "iterator test str"
i = iter(string)

count = 0
while True:
    try:
        print(next(i), end='')
    except StopIteration:
        break
