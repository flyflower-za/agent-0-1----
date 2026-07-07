import numpy as np

def print_separator(title):
    print(f"\n{'='*20} {title} {'='*20}")

# 模拟一个班级的成绩单：3个学生，4门课
scores = np.array([
    [80, 90, 85, 95],  # Student A
    [70, 75, 65, 80],  # Student B
    [60, 100, 60, 40]  # Student C (偏科战神)
])

print("成绩单 (Rows=Students, Cols=Subjects):\n", scores)

# 1. 基础统计
print_separator("1. Basic Stats")
print(f"全班最高分: {scores.max()}")
print(f"全班平均分: {scores.mean():.2f}")
# argmax: 找出最大值的索引（谁考了最高分？）不分行列拍平找
print(f"最高分的位置索引: {scores.argmax()}") 

# 2. Axis (轴) 操作 - 重点！
print_separator("2. Axis Operations")
# 计算每个学生的平均分 -> 沿着 axis=1 (横向) 操作
student_averages = scores.mean(axis=1)
print("每个学生的平均分:", student_averages)

# 计算每门课的最高分 -> 沿着 axis=0 (纵向) 操作
subject_max = scores.max(axis=0)
print("每门课的最高分:", subject_max)

# 3. 变形 (Reshape)
print_separator("3. Reshape")
# 生成一个 0-11 的数组
arr = np.arange(12)
print("原始一维数组:", arr)

# 变成 3x4 矩阵
mat_3x4 = arr.reshape(3, 4)
print("\nReshape to (3, 4):\n", mat_3x4)

# 变成 4x3 矩阵
mat_4x3 = arr.reshape(4, 3)
print("\nReshape to (4, 3):\n", mat_4x3)

# 展平 (Flatten) -> 变回一维
print("\nFlattened:", mat_3x4.flatten())

# 转置 (Transpose) -> 行变列，列变行
print("\nTranspose (转置):\n", mat_3x4.T)
