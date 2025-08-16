# PARENT CLASS 
class Person:
    #CONSTRACTOR
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def display(self):
        print(f"Name: {self.name}, ID: {self.id}")
        
emp = Person("ankush", 123456)
emp.display()  # Output: Name: ankush, ID: 123456

# CHILD CLASS 
class Employee(Person):
    def __init__(self, name, id, age):
        super().__init__(name, id)
        self.age = age
    def Print(self):
        print("Employee Class is called ")
        
# Emp_details = Employee("Priyansh",987654)
emp1 = Employee("PK",545,20)
print(emp1.age)
emp1.display()
# Emp_details.display()
# Emp_details.Print()
# print(dir(Emp_details))
