class Employee:
    """
    class Employee
    """
    def __init__(self, age, name, salary):
        self.age = age
        self.name = name
        self.salary = salary
    
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.salary



class Manager(Employee):
    """"
    Manager class
    """
    def __init__(self, name, age, salary):
        super().__init__(name=name, age=age, salary=salary)
    
    def set_bonus(self, bonus_percent):
        self.bonus = self.salary * bonus_percent / 100
        self.salary = self.salary + self.bonus
    

m = Manager('ganesh', 21, 300000)
print(m.salary)

m.set_bonus(10)
print(m.salary)
