class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f"{self.first} {self.last}"

emp_1 = Employee("Kolawole", "Ayodeji", 2000000)
emp_2 = Employee("Damilola", "Ayobami", 1000000)

# print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email)

print(emp_1.fullname())
# print(emp_2.fullname())
Employee.fullname(emp_1)