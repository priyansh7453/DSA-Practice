class Animal:
    def speak(self):
        print("Some sound")
        
    def eat(self):
        print("Eating food")
    
class dog(Animal):
    def bark(self):
        print("Woof Woof")
        
    def eat(self):
        print("Dog is eating bones")

class cat(Animal):
    def meow(self):
        print("Meow Meow")
        
    def eat(self):
        print("Cat is eating fish")

# Create instances of dog and cat
dog1 = dog()
dog1.speak()
dog1.bark()
dog1.eat()
cat1 = cat()
cat1.speak()
cat1.meow()
cat1.eat()
print("Dog and Cat classes demonstrate inheritance and method overriding.")
        