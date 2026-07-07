import numpy as np

def print_separator(title):
    print(f"\n{'='*20} {title} {'='*20}")

# 1. 简单的逐元素运算 (Element-wise)
print_separator("1. Element-wise Operation")
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

# 每一个对应位置相加/乘
print(f"a: {a}")
print(f"b: {b}")
print("a + b =", a + b)
print("a * b =", a * b)

# 2. 标量广播 (最简单的情况)
print_separator("2. Scalar Broadcasting")
# 想象一下：把 5 广播到了矩阵的每一个角落
matrix = np.array([
    [1, 2],
    [3, 4]
])
print("Original Matrix:\n", matrix)
print("\nMatrix + 10:\n", matrix + 10)

# 3. 向量广播 (常见场景)
print_separator("3. Vector Broadcasting")
A = np.array([
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]) # Shape (3, 3)

row_vec = np.array([10, 20, 30]) # Shape (3,)

print("Matrix A (3x3):\n", A)
print("Row Vector (3,):\n", row_vec)

# 每一行都会加上这个向量
# Row 0: [1,1,1] + [10,20,30] = [11,21,31]
# Row 1: [2,2,2] + [10,20,30] = [12,22,32]...
result = A + row_vec
print("\nA + Row Vector:\n", result)

# 4. 维度不匹配演示
print_separator("4. Incompatible Shapes")
try:
    # 试图把一个 2个元素的向量加到 3列的矩阵上 -> 报错
    wrong_vec = np.array([1, 2])
    print(A + wrong_vec)
except ValueError as e:
    print("❌ Error as expected:", e)
