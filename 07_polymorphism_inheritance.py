#Method Overriding
class Animal:
    def speak(self):
        print("Animal make sound")
class Dog(Animal):
    def speak(self):
        print("Bark")


class Cat(Animal):
    def speak(self):
        print("Meow")

animal=[Dog(),Cat(),Animal()]
for a in animal:
    a.speak()
        
