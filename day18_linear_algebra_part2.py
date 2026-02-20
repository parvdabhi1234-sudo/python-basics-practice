# ===== LINEAR ALGEBRA PART 2 =====
# Topics:
# 1 Matrix Multiplication
# 2 Transpose
# 3 Identity Matrix
# 4 Determinant

print("=== MATRIX MULTIPLICATION ===")

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = [
    [
        A[i][0]*B[0][j] + A[i][1]*B[1][j]
        for j in range(2)
    ]
    for i in range(2)
]

print("Matrix Multiplication:", result)


print("\n=== TRANSPOSE ===")

transpose = [
    [A[j][i] for j in range(2)]
    for i in range(2)
]

print("Transpose of A:", transpose)


print("\n=== IDENTITY MATRIX ===")

identity = [
    [1 if i==j else 0 for j in range(3)]
    for i in range(3)
]

print("3x3 Identity Matrix:", identity)


print("\n=== DETERMINANT (2x2) ===")

# Formula: ad - bc

det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
print("Determinant of A:", det)
