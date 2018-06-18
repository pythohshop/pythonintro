"""
Simple try except example
"""

# Try block 
try:
    count = 0
    while True:
        print(count)
        count += 1

# Finally block 
except (KeyboardInterrupt):
    print("You know better than to go on a infinite spree")

# Finally block 
finally:
    print("Congratulations you just averted a memory crisis")