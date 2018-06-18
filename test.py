def reverse(string):
    for i in range(len(string)):
        print(string[len(string) - i - 1])

reverse("Hello")