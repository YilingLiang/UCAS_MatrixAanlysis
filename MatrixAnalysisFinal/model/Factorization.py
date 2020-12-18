#coding:utf8
import numpy as np
import sys,os
import math

from utils.matrixFromFile import load_array
from utils import auxiliary

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
    return (Q, R)

def givens_rotation(A):
    """Givens变换"""
    (r, c) = np.shape(A)
    Q = np.identity(r)
    R = np.copy(A)
    (rows, cols) = np.tril_indices(r, -1, c)
    for (row, col) in zip(rows, cols):
        if R[row, col] != 0:  # R[row, col]=0则c=1,s=0,R、Q不变
            r_ = np.hypot(R[col, col], R[row, col])  # d
            c = R[col, col]/r_
            s = -R[row, col]/r_
            G = np.identity(r)
            G[[col, row], [col, row]] = c
            G[row, col] = s
            G[col, row] = -s
            R = np.dot(G, R)  # R=G(n-1,n)*...*G(2n)*...*G(23,1n)*...*G(12)*A
            Q = np.dot(Q, G.T)  # Q=G(n-1,n).T*...*G(2n).T*...*G(23,1n).T*...*G(12).T
    return (Q, R)

def householder_reflection(A):
    """Householder变换"""
    (r, c) = np.shape(A)
    Q = np.identity(r)
    R = np.copy(A)
    for cnt in range(r - 1):
        x = R[cnt:, cnt]
        e = np.zeros_like(x)
        e[0] = np.linalg.norm(x)
        u = x - e
        v = u / np.linalg.norm(u)
        Q_cnt = np.identity(r)
        Q_cnt[cnt:, cnt:] -= 2.0 * np.outer(v, v)
        R = np.dot(Q_cnt, R)  # R=H(n-1)*...*H(2)*H(1)*A
        Q = np.dot(Q, Q_cnt)  # Q=H(n-1)*...*H(2)*H(1)  H为自逆矩阵
    return (Q, R)


if __name__ == "__main__":
    # 一个测试
    np.set_printoptions(precision=4, suppress=True)
    A = np.array([
            [1, 0, - 1],
            [1, 2, 1],
            [1., 1., -3],
            [0, 1, 1]
        ])
    print("QR分解")
    (Q, R) = gram_schmidt(A)
    # print(Q)
    # print(R)
    print("Matrix Q:")
    auxiliary.print_array(Q)
    print("Matrix R:")
    auxiliary.print_array(R)
    print("Matrix QR:")
    print (np.dot(Q,R), "\n")# 验证分解是否正确

    print("Givens")
    (Q, R) = givens_rotation(A)
    print("Matrix Q:")
    auxiliary.print_array(Q)
    print("Matrix R:")
    auxiliary.print_array(R)
    print("Matrix QR:")
    print (np.dot(Q,R), "\n")

    print("HouseHold")
    (Q, R) = householder_reflection(A)
    print("Matrix Q:")
    auxiliary.print_array(Q)
    print("Matrix R:")
    auxiliary.print_array(R)
    print("Matrix QR:")
    print (np.dot(Q,R))