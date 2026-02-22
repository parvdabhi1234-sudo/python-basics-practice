print("\n=== PRACTICE QUESTIONS ===")

# Q1 derivative of x^5

def d1(x):
    return 5*(x**4)
print("Q1 derivative of x^5 at 2:", d1(2))

# Q2 derivative of 7x^3

def d2(x):
    return 21*(x**2)
print("Q2 derivative of 7x^3 at 1:", d2(1))

# Q3 slope of x^2 at x=4

print("Q3 slope at 4:", derivative_f(4))

# Q4 approximate slope at x=5

print("Q4 approximate slope at 5:", approximate_slope(5))

# Q5 critical point of x^2

print("Q5 critical point of x^2: x = 0")

print("\n--- Day 20 Calculus Part 2 Complete ---")
