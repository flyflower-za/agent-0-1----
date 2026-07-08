import numpy as np

def print_separator(title):
    print(f"\n{'='*20} {title} {'='*20}")

# 1. 基础数组创建
print_separator("1. List vs Array")
py_list = [1, 2, 3]
np_arr = np.array([1, 2, 3])
print(f"Python List: {py_list}, Type: {type(py_list)}")
print(f"NumPy Array: {np_arr}, Type: {type(np_arr)}")

# 2. 也是常用的特殊矩阵
print_separator("2. Special Matrices")
# 3行4列的全0矩阵
zeros = np.zeros((3, 4))
print("Zeros (3x4):\n", zeros)

# 2行3列的全1矩阵
ones = np.ones((2, 3))
print("\nOnes (2x3):\n", ones)

# 3. 随机矩阵 (模拟神经网络初始化)
print_separator("3. Random Matrix")
# 生成 3x3 的随机数 (0到1之间)
rand_mat = np.random.rand(3, 3)
print("Random (3x3):\n", rand_mat)

# 随机整数 (0到100之间，4行2列)
rand_int = np.random.randint(0, 100, (4, 2))
print("\nRandom Integers (4x2):\n", rand_int)

# 4. 序列生成
print_separator("4. Sequence Generation")
# 0到10，步长为2
seq = np.arange(0, 10, 2)
print("Arange (0, 10, 2):", seq)

# linspace: 0到10之间均匀取5个点
lin = np.linspace(0, 10, 5)
print("Linspace (5 points between 0-10):", lin)

# 5. 查看属性
print_separator("5. Array Attributes")
data = np.ones((5, 3))
print("Data:\n", data)
print(f"维度 (ndim): {data.ndim}")
print(f"形状 (shape): {data.shape}")
print(f"类型 (dtype): {data.dtype}")
