# ===== LINEAR ALGEBRA PART 1 =====
# Topics:
# 1 Vectors
# 2 Vector Addition
# 3 Dot Product
# 4 Matrices

print("=== VECTORS ===")

v1 = [1, 2, 3]
v2 = [4, 5, 6]

print("Vector 1:", v1)
print("Vector 2:", v2)


print("\n=== VECTOR ADDITION ===")

add = [v1[i] + v2[i] for i in range(len(v1))]
print("Addition:", add)


print("\n=== DOT PRODUCT ===")

dot = sum(v1[i] * v2[i] for i in range(len(v1)))
print("Dot Product:", dot)


print("\n=== MATRICES ===")

matrix1 = [
    [1, 2],
    [3, 4]
]

matrix2 = [
    [5, 6],
    [7, 8]
]

print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)


print("\n=== MATRIX ADDITION ===")

matrix_add = [
    [matrix1[i][j] + matrix2[i][j] for j in range(2)]
    for i in range(2)
]

print("Matrix Addition:", matrix_add)
