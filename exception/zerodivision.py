def divide(a, b):
    try:
        result = a / b
        return result
    except (ZeroDivisionError):
        return "Cannot divide by zero brother"

print(divide(1, 0))