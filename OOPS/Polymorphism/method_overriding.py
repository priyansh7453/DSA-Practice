# Method Overriding \
# Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass.
class Animal:   
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
    
obj = Dog()
obj.sound()  # Output: Dog barks

obj2 = Animal()
obj2.sound()  # Output: Animal makes a sound