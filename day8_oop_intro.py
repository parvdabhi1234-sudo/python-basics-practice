# OOP Intro

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

s1 = Student("Parv", 20)
s1.display()


# -------- Questions --------

# Q1 Create class Car

class Car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("Brand:", self.brand)

c1 = Car("BMW")
c1.show()

# Q2 Class Rectangle area

class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Area:", self.l*self.b)

r = Rectangle(4,5)
r.area()
