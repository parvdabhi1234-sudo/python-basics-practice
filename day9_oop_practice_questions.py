# ===== PRACTICE QUESTIONS ===== #

# Q1 Car class

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)

c = Car("BMW", 120)
c.show()

print("\n--- Car Class Question End ---\n")

# Q2 Shape -> Rectangle

class Shape:
    pass

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Area:", self.l * self.b)

r = Rectangle(4,5)
r.area()

print("\n--- Rectangle Question End ---\n")

# Q3 Employee private salary

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print("Name:", self.name)
        print("Salary:", self.__salary)

e = Employee("Rahul", 40000)
e.show()

print("--- Employee Question End ---\n")
