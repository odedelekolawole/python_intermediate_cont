class SoftwareEngineer:

    # class attibute
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        # instances attribute
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    # Instance method
    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self, language):
        print(f"{self.name} is writing in {language}...")
        
    def information(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information
    
    # dunder method
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


# Instances
se1 = SoftwareEngineer("Kolawole", 20, "Junior", 2000000)
print(se1.name, se1.age)
print(SoftwareEngineer.alias)
se2 = SoftwareEngineer("Ayodeji", 25, "Senior", 4000000)
se3 = SoftwareEngineer("Ayodeji", 27, "Senior", 4000000)
print(se2.age)
print(SoftwareEngineer.alias)

se1.code()
se1.code_in_language("Python")
se2.code_in_language("C++")

se1.information()
print(se1.information())
print(se1)
print(se2 == se3)

print(se1.entry_salary(24))
print(SoftwareEngineer.entry_salary(27))


