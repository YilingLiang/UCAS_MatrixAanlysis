### Sherman-Morrison 定理

> 设矩阵 $A \in R^{n\times n}$ 可逆，$c,d\in R^n$ ，若 $1+d^TA^{-1}c \neq 0$ ，则 $A$ 的秩 $1$ 矫正矩阵 $A+cd^T$ 可逆，且：
> $$
> (A+cd^T)^{-1}=A^{-1}-\frac{A^{-1}cd^TA^{-1}}{1+d^TA^{-1}c}
> $$
> 更一般地，如果 $C,D \in R^{n\times k}$ ，且 $I+D^TA^{-1}C$ 存在，则有：
> $$
> (A+CD^T)^{-1}=A^{-1}-A^{-1}C(I+D^TA^{-1}C)^{-1}D^TA^{-1}
> $$
> 

