# -*- coding:UTF-8 -*-
import numpy as np
import os,sys
import argparse
from utils import matrixFromFile
from utils import auxiliary
from model.LU import LU_factorization
from model.Gram_Schmidt import gram_schmidt
from model.HouseHold import householder_reflection
from model.Givens import givens_rotation
from model.URV import URV_factorization

# 获取当前工作路径
path = os.getcwd()

ap = argparse.ArgumentParser(description="Five Reduction Methods")
#选择使用的分解算法，可选项'LU','QR','HR','GR','URV'
ap.add_argument("--model", type=str, choices=['LU','QR','HR','GR','URV'], default="LU",
                help="5 choices in ['LU','QR','HR','GR','URV'], \
                     LU->LU factorization, \
                     QR->Schmidt Procedure, \
                     HR->Housholder Reduction, \
                     GR->Givens Reduction, \
                     URV->URV factorization")

ap.add_argument("--input", type=str, default="./data/LU.txt",
                help="input example file path.")

args = ap.parse_args()


if __name__ == "__main__":
    input_file=path+'/'+args.input
    # print(input_file)
    matrix= matrixFromFile.load_array(input_file, args.model)
    m, n = matrix.shape
    if matrix.size ==0:
        print("input Error!")
        sys.exit()

    if args.model == "LU":
        print("\nYou have selected LU Factorization, the input should be a square matrix.\n")
    elif args.model == "QR":
        # 首先判断矩阵是否是列线性无关的
        mat_rank = auxiliary.rank_of_matrix(matrix)
        if mat_rank<n:
            print("Error!\nThe matrix with linearly dependent columns Can Not be uniquely factored as A=QR!\n\n")
            sys.exit()

    print("="*50,"\norigin matrix type: {m} * {n}" .format(m=m,n=n),"\nOrigin Matrix A = ")
    auxiliary.print_array(matrix)
    print("="*50, "\nResult:")
    if args.model == "LU":
        print("The input Matrix：")
        auxiliary.print_array(matrix)
        L, U, P = LU_factorization(matrix)
        print("The factorization Results：")
        print("Matrix L:")
        auxiliary.print_array(L)
        print("Matrix U:")
        auxiliary.print_array(U)
        print("Matrix P:")
        auxiliary.print_array(P)
        print("Matrix PLU:")  # 验证结果是否正确
        print(P.dot(L).dot(U))

    elif args.model == "QR":
        print("The input Matrix：")
        auxiliary.print_array(matrix)
        Q, R = gram_schmidt(matrix)
        print("The factorization Results：")
        print("Matrix Q:")
        auxiliary.print_array(Q)
        print("Matrix R:")
        auxiliary.print_array(R)
        print("Matrix QR:")
        print(np.dot(Q, R), "\n")
        
    elif args.model == "HR":
        print("The input Matrix：")
        auxiliary.print_array(matrix)

        Q, R = householder_reflection(matrix)
        print("The factorization Results：")
        print("Matrix Q:")
        auxiliary.print_array(Q)
        print("Matrix R:")
        auxiliary.print_array(R)

        print("Matrix QR:")  # 验证结果是否正确
        print(np.dot(Q, R), "\n")

    elif args.model=="GR":
        print("The input Matrix：")
        auxiliary.print_array(matrix)

        Q, R = givens_rotation(matrix)
        print("The factorization Results：")
        print("Matrix Q:")
        auxiliary.print_array(Q)
        print("Matrix R:")
        auxiliary.print_array(R)
        print("Matrix QR:")  # 验证结果是否正确
        print(np.dot(Q, R), "\n")

    elif args.model == "URV":
        print("Matrix A:")
        auxiliary.print_array(matrix)
        U, R, V = URV_factorization(matrix)
        print("Factoriaztion results:")
        print("Matrix U:")
        auxiliary.print_array(U)
        print("Matrix R:")
        auxiliary.print_array(R)
        print("Matrix V:")
        auxiliary.print_array(V)
        print("Matrix URV:")
        auxiliary.print_array(U.dot(R).dot(V.T))