# ===== CALCULUS PART 1 =====
# Topics:
# 1 Functions
# 2 Limits (Basic Concept)

print("=== FUNCTIONS ===")

# Example function: f(x) = x^2

def f(x):
    return x**2

print("f(2) =", f(2))
print("f(3) =", f(3))
print("f(5) =", f(5))


print("\n=== LIMIT CONCEPT ===")

# Limit example:
# lim x→2 (x^2)

# Checking values near 2

values = [1.9, 1.99, 1.999, 2, 2.001, 2.01]

for v in values:
    print("f(", v, ") =", f(v))

print("\nAs x approaches 2, f(x) approaches 4")


print("\n=== PRACTICE QUESTIONS ===")

# Q1 Function: g(x) = 2x + 3

def g(x):
    return 2*x + 3

print("Q1 g(4) =", g(4))

# Q2 Check limit near 3 for h(x)=x^2

def h(x):
    return x**2

vals = [2.9, 2.99, 3, 3.01]
for v in vals:
    print("Q2 h(", v, ") =", h(v))

# Q3 Function cube

def cube(x):
    return x**3

print("Q3 cube(2) =", cube(2))

# Q4 Function 5x - 1

def linear(x):
    return 5*x - 1

print("Q4 linear(3) =", linear(3))

# Q5 Function absolute value

def absolute(x):
    return abs(x)

print("Q5 absolute(-7) =", absolute(-7))

print("\n--- Day 19 Calculus Part 1 Complete ---")
