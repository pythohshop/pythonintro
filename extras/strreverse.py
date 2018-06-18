# Reversing a string 
def reverse(s):
    length = len(s)
    count = length - 1
    while count >= 0:
        print(s[count], end='')
        count -= 1
    print()

# Driver function testing
def main():
    s = "this is a string to reverse"
    reverse(s)

main()