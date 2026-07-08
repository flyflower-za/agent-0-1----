import numpy as np

def print_separator(title):
    print(f"\n{'='*20} {title} {'='*20}")

# 创建一个 3x4 的矩阵作为练习素材
matrix = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])

print("原始矩阵:\n", matrix)

# 1. 基础索引
print_separator("1. Basic Indexing")
# 取出一行 (第0行)
row_0 = matrix[0] 
print("第0行:", row_0)

# 取出一个具体的值 (第1行，第2列 -> 数字7)
# 注意：索引从0开始
val = matrix[1, 2]
print("matrix[1, 2] =", val)

# 2. 矩阵切片 (重点)
print_separator("2. Slicing")
# 切前两行 (0, 1行)，前两列 (0, 1列)
sub_matrix = matrix[0:2, 0:2]
print("前两行前两列:\n", sub_matrix)

# 🔥 常用技巧：取某一列
# [:, 2] 意思是：所有行，第2列
col_2 = matrix[:, 2]
print("只取第2列 (Col index 2):\n", col_2)

# 3. 布尔索引 (魔法)
print_separator("3. Boolean Indexing")
scores = np.array([55, 90, 45, 80, 72, 30])
print("分数列表:", scores)

# 找出所有及格的
passed_mask = scores >= 60
print("及格掩码 (Mask):", passed_mask)
print("及格的分数:", scores[passed_mask])

# 快速修改数据：把不及格的都改成 60
scores[scores < 60] = 60
print("补考修正后:", scores)
