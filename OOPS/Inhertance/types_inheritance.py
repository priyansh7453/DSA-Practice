## Types of Inheritance
# Inheritance is a fundamental concept in object-oriented programming that allows a class to inherit properties and methods from another class.


# 1, Single Inheritance
class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Parent Name:", self.name)
        
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        super().display()
        print("Child Age:", self.age)
        
# Example usage
parent = Parent("John")
parent.display()    
child = Child("Alice", 10)
child.display()

#2, Multiple Inheritance
class Father:
    def __init__(self, name):
        self.father_name = name

    def display(self):
        print("Father Name:", self.father_name)
        
class Mother:
    def __init__(self, name):
        self.mother_name = name

    def display(self):
        print("Mother Name:", self.mother_name)

class Child(Father, Mother):
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.child_name = child_name

    def display(self):
        Father.display(self)
        Mother.display(self)
        print("Child Name:", self.child_name)   
        
# Example usage
father = Father("John") 
mother = Mother("Jane")
father.display()
mother.display()
child = Child("John", "Jane", "Alice")
child.display()


# 3, Multilevel Inheritance