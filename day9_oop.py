# 1) Class & Object

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Parv", 20)
s1.show()

print("\n--- Student Info End ---\n")

# 2) Inheritance

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()

print("\n--- Inheritance Example End ---\n")

# 3) Polymorphism

class Bird:
    def sound(self):
        print("Bird chirps")

class Cat:
    def sound(self):
        print("Cat meows")

for obj in (Bird(), Cat()):
    obj.sound()

print("\n--- Polymorphism Example End ---\n")

# 4) Encapsulation

class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)

b = Bank(5000)
b.show_balance()

print("\n--- Encapsulation Example End ---\n")
