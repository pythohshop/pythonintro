"""
Example of simple custom exception
"""

class MyCustomException(Exception):
    pass



try:
    # Some condition 
    raise MyCustomException

except MyCustomException:
    # do something or just pass
    pass

finally:
    # do something 
    # finally is optional 