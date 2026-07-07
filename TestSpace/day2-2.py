import numpy as np


matrix = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])


print(matrix[0])

print(matrix[1,2])

print(matrix[:,1])


scores = np.array([55, 90, 45, 80, 72, 30])

passed = scores > 60

print("及格的分数有:", scores[passed])
print("及格掩码为:", passed)

scores[scores<60] = 60
print("补考修正后:", scores)
