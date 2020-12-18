
import numpy as np
import sys,os
import math

from utils.matrixFromFile import load_array
from utils import auxiliary

path = os.getcwd()

def gram_schmidt(A):
    """Gram-schmidt正交化"""
    Q=np.zeros_like(A)
    cnt = 0
    for a in A.T:
        u = np.copy(a)
        for i in range(0, cnt):
            u -= np.dot(np.dot(Q[:, i].T, a), Q[:, i]) # 减去待求向量在以求向量上的投影
        e = u / np.linalg.norm(u)  # 归一化
        Q[:, cnt] = e
        cnt += 1
    R = np.dot(Q.T, A)
    return Q, R

if __name__ == "__main__":
    input_file = "../data/GramSchmidt.txt"
    # matrix, = load_array(input_file, "QR")
    matrix = np.array([
        [1, 0, - 1],
        [1, 2, 1],
        [1., 1., -3],
        [0, 1, 1]
    ])
    m, n = matrix.shape
    print("The input Matrix：")
    auxiliary.print_array(matrix)
    if matrix.size ==0:
        print("input Error!")
        sys.exit()
    mat_rank = auxiliary.rank_of_matrix(matrix)
    if mat_rank < n:
        print("Error, the matrix with linearly dependent columns Can Not be factored as A=QR!\n\n")
        sys.exit()

    Q, R = gram_schmidt(matrix)
    print("The factorization Results：")
    print("Matrix Q:")
    auxiliary.print_array(Q)
    print("Matrix R:")
    auxiliary.print_array(R)
    print("Matrix QR:")
    print(np.dot(Q, R), "\n")
    # print(Q.dot(R))