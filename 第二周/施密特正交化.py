import numpy as np

with open("正交化向量.txt") as f:
    vectors = []
    for line in f:
        vector = list(map(int, line.strip().split()))
        vectors.append(vector)

vectors = np.array(vectors).astype(np.float64)

print(f"正交化前结果：\n{vectors}")

for i in range(len(vectors)):
    for j in range(i):
         vectors[i] -= np.dot(vectors[i], vectors[j]) / np.dot(vectors[j], vectors[j]) * vectors[j]

print(f"正交化后结果：\n{vectors}")

for i in range(len(vectors)):
    for j in range(i):
        print(f"{i}与{j}点乘结果：{np.dot(vectors[i], vectors[j])}")

print(f"所得矩阵的秩:{np.linalg.matrix_rank(vectors)}")