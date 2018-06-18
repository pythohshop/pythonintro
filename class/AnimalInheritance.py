class Animal:
    def __init__(self, name, place, sound):
        self.name = name
        self.place = place
        self.sound = sound
    
    def get_name(self):
        return self.name
    
    def get_place(self):
        return self.place
    
    def get_sound(self):
        return self.sound
    
    def __str__(self):
        return (self.get_name() + ' ' + self.get_place() + ' ' + self.get_sound())


class Dog(Animal):
    def __init__(self, name, place, sound):
        super().__init__(name, place, sound)

class Cat(Dog):    # Cat is dog really?
    def __init__(self, name, place, sound):
        super().__init__(name, place, sound)

my_dog = Dog('husky', 'kennel', 'bark')
print(my_dog)
