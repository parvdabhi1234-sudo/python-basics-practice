print("\n=== PRACTICE QUESTIONS ===")

# Q1 Multiply [[1,0],[0,1]] with [[2,3],[4,5]]

I=[[1,0],[0,1]]
M=[[2,3],[4,5]]
print("Q1:", [
    [I[i][0]*M[0][j] + I[i][1]*M[1][j] for j in range(2)]
    for i in range(2)
])

# Q2 Transpose of [[1,2,3],[4,5,6]]

mat=[[1,2,3],[4,5,6]]
print("Q2:", [[mat[j][i] for j in range(2)] for i in range(3)])

# Q3 Determinant of [[2,3],[1,4]]

print("Q3:", 2*4 - 3*1)

# Q4 Identity 2x2

print("Q4:", [[1 if i==j else 0 for j in range(2)] for i in range(2)])

# Q5 Scalar multiply matrix

print("Q5:", [[2*x for x in row] for row in [[1,2],[3,4]]])

print("\n--- Day 18 Linear Algebra Part 2 Complete ---")
