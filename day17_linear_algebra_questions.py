print("\n=== PRACTICE QUESTIONS ===")

# Q1 Add [2,3] + [4,5]

a=[2,3]
b=[4,5]
print("Q1:", [a[i]+b[i] for i in range(2)])

# Q2 Dot product of [1,2] and [3,4]

print("Q2:", 1*3 + 2*4)

# Q3 Matrix addition 2x2

m1=[[1,1],[1,1]]
m2=[[2,2],[2,2]]
print("Q3:", [[m1[i][j]+m2[i][j] for j in range(2)] for i in range(2)])

# Q4 Print vector length

v=[3,4]
length=(v[0]**2+v[1]**2)**0.5
print("Q4 Vector Length:", length)

# Q5 Scalar multiplication

print("Q5:", [2*x for x in [1,2,3]])

print("\n--- Day 17 Linear Algebra Part 1 Complete ---")
