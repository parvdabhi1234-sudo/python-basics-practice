# Day 4 - Functions detailed

# 1 Simple function

def welcome():
    print("Welcome to AI/ML journey")

welcome()

# 2 Function with parameters

def greet(name, age):
    print("Hello", name)
    print("Age:", age)

greet("Parv", 19)

# 3️ Function with return value

def add(a, b):
    return a + b

result = add(10, 5)
print("Sum:", result)

# 4️ Default parameter

def country(name="India"):
    print("Country:", name)

country()
country("USA")

# 5️ Multiple return values

def operations(a, b):
    return a+b, a-b, a*b

sum_, sub_, mul_ = operations(8, 4)
print("Sum:", sum_)
print("Subtract:", sub_)
print("Multiply:", mul_)

# 6️ Lambda function

square = lambda x: x*x
print("Square:", square(6))

# 7️ Lambda with 2 inputs

max_num = lambda a, b: a if a>b else b
print("Max:", max_num(7, 3))
