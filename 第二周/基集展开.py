import numpy as np

with open("基集展开向量.txt") as f:
    base_vectors = []
    for line in f:
        base_vector = list(map(int, line.strip().split()))
        base_vectors.append(base_vector)

base_vectors = np.array(base_vectors).astype(np.float64)

print(f"基向量：\n{base_vectors}")

vector = np.array([1, 2, 2]).astype(np.float64)
print(f"待展开向量:\n{vector}")

if base_vectors.shape[0] != base_vectors.shape[1]:
    raise ValueError("基集展开向量矩阵必须是方阵")

r_vectors = np.linalg.inv(base_vectors)

print(r_vectors)

result = np.dot(r_vectors, vector)

print(f"各向量系数：{result}")

reconstructed_vector = np.dot(base_vectors, result)
print(f"重构后的向量：{reconstructed_vector}")
