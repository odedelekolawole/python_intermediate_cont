# Inherits. extend, overide
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
        

    def worker(self):
        print(f"{self.name} is working...")



class SofwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def worker(self):
        print(f"{self.name} is coding...")

    def debug(self):
        print(f"{self.name} is debuging")

class Designer(Employee):
    
    def worker(self):
        print(f"{self.name} is designing...")

    def draw(self):
        print(f"{self.name} is drawing...")

se = SofwareEngineer("Kolawole", 20, 5000000, "Junior")
se.worker()
# print(se.level)
# print(se.debug())
# se.draw()

d = Designer("Ayodeji", 25, 3000000)
d.worker()
# d.draw()




#Polymorphism


