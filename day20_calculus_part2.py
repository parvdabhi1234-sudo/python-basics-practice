# ===== CALCULUS PART 2 =====
# Topics:
# 1 Derivative Introduction
# 2 Power Rule
# 3 Slope Concept
# 4 Basic Optimization Idea

print("=== DERIVATIVE INTRODUCTION ===")

# Function f(x) = x^2

def f(x):
    return x**2

# Derivative using power rule

# d/dx (x^2) = 2x
def derivative_f(x):
    return 2*x

print("f(3) =", f(3))
print("f'(3) =", derivative_f(3))


print("\n=== SLOPE CONCEPT ===")

# Approximate slope using small change (h)

def approximate_slope(x, h=0.0001):
    return (f(x+h) - f(x)) / h

print("Approximate slope at x=3:", approximate_slope(3))
print("Actual derivative at x=3:", derivative_f(3))


print("\n=== POWER RULE EXAMPLES ===")

# g(x) = x^3 → derivative = 3x^2

def g(x):
    return x**3

def derivative_g(x):
    return 3*x**2

print("g(2) =", g(2))
print("g'(2) =", derivative_g(2))


# h(x) = 5x^4 → derivative = 20x^3

def h(x):
    return 5*(x**4)

def derivative_h(x):
    return 20*(x**3)

print("h(1) =", h(1))
print("h'(1) =", derivative_h(1))


print("\n=== BASIC OPTIMIZATION IDEA ===")

# If derivative = 0 → possible minimum or maximum
# Example: f'(x) = 2x
# Set 2x = 0 → x = 0 (minimum point)

print("Minimum of x^2 occurs at x = 0")
