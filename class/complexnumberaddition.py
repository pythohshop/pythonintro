"""
Example of operator overloading in python 
"""


class Complex:
    def __init__(self, real_value, img_value):
        self.real = real_value
        self.img = img_value
    
    def __add__(self, other):
        self.real = self.real + other.real 
        self.img = self.img + other.img

        return self
    
    def __str__(self): # Assuming both real and img are positive values
        return str(self.real) + ' +' + ' j' + str(self.img)
    
# Driver program to test the Complex class

def main():
    complex1 = Complex(1, 2)
    complex2 = Complex(3, -4)

    complex3 = complex1 + complex2
    print(complex3)


main()
