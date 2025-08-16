### Access Modifier--->Encapsulation
## private
class PersonPrivate:
    ## constructor
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def display_info(self):
        print(f"the person name is {self.__name} and the age is {self.__age}")

person1=PersonPrivate("Krish",25)
person1.display_info()
# print(dir(person1))  # Shows all attributes, including protected ones
print(person1._PersonPrivate__age)      # But it is not good techniques beacuse anyone to use private variable so we cannot use 

class PersonProcted:
    ## constructor
    def __init__(self,name,age):
        self._name=name
        self._age=age

    def display_info(self):
        print(f"the person name is {self._name} and the age is {self._age}")
        
person2=PersonProcted("Ankush",32)
person2.display_info()

print(person2._age)


class PersonPublic:
    ## constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print(f"the person name is {self.name} and the age is {self.age}")  

person3=PersonPublic("Priyansh",32)
person3.display_info()