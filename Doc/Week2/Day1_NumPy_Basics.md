# Week 2 Day 1: NumPy 基础与数组创建

## 🎯 学习目标
掌握 NumPy 的核心对象 `ndarray`，学会多种创建矩阵的方法，并理解数组的基本属性。

## 📘 详细介绍

### 为什么要用 NumPy?
NumPy (Numerical Python) 是 Python 数据科学生态的基石。
1.  **速度快**: 核心用 C 语言编写，比 Python 原生 List 快 10-100 倍。
2.  **内存省**: 紧凑的存储结构。
3.  **向量化**: 支持对整个数组进行数学运算，无需编写循环。

### 核心：ndarray
NumPy 的核心数据结构是 `ndarray` (N-dimensional Array)。与 Python List 不同，ndarray 要求数组内所有元素的**类型必须相同**（通常是数字），这使得它非常适合进行高效的数学计算。

### 常用创建方法
1.  `np.array()`: 从 Python List 转换。
2.  `np.zeros()`: 创建全 0 矩阵（初始化模型权重常用）。
3.  `np.ones()`: 创建全 1 矩阵。
4.  `np.random.rand()`: 生成 0-1 之间的随机数。
5.  `np.arange()`: 类似 Python 的 range，但生成的是数组。

### 关键属性 (The "Three Dimensions")
拿到一个未知数据，第一时间要看它的属性：
-   `.ndim`: 维度 (Dimension)，是几维数组？
-   `.shape`: 形状，几行几列？
-   `.dtype`: 数据类型，是整数还是浮点数？

## 💻 练习代码
请运行同目录下的 `day1_basics.py` 文件，观察输出结果。
