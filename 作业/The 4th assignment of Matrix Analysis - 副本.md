### 矩阵分析第四次作业

#### 课件6 练习4

**解： (a)**
$$
\begin{align}
A(e_1,e_2,e_3)
=\left(
\begin{array}{rrr}
1 & 2 & -1   \\
0 & -1 & 0  \\
1 & 0 & 7 
\end{array}
\right)
=(e_1,e_2,e_3)\left(
\begin{array}{rrr}
1 & 2 & -1   \\
0 & -1 & 0  \\
1 & 0 & 7 
\end{array}
\right)\\
\end{align}
$$
故
$$
[A]_{\mathcal{S}}=\left(
\begin{array}{rrr}
1 & 2 & -1   \\
0 & -1 & 0  \\
1 & 0 & 7 
\end{array}
\right)
$$
**(b)** 因 
$$
A\mathcal{S}^\prime=\left(
\begin{array}{rrr}
1 & 3 & 2   \\
0 & -1 & -1  \\
1 & 1 & 8 
\end{array}
\right)=\mathcal{S}^\prime\left(
\begin{array}{rrr}
1 & 4 & 3   \\
-1 & -2 & -9  \\
1 & 1 & 8 
\end{array}
\right)
$$
故
$$
[A]_{\mathcal{S}^\prime}=\left(
\begin{array}{rrr}
1 & 4 & 3   \\
-1 & -2 & -9  \\
1 & 1 & 8 
\end{array}
\right)
$$
由于
$$
\mathcal{S}^{\prime}=I\mathcal{S}^{\prime}
$$
则基 $\mathcal{S}=I$ 到 基 $\mathcal{S}^{\prime}$ 的过渡矩阵为 $\mathcal{S}^{\prime}$，从而由定理可知 $Q=\mathcal{S}^{\prime}$ ，即
$$
Q=\left(
\begin{array}{rrr}
1 & 1 & 1   \\
0 & 1 & 1  \\
0 & 0 & 1 
\end{array}
\right)\\
$$

#### 课件6 练习 7

**解： (a)** 任意取 $e_i\in \mathcal{X},i=1,2$ ，有 $T(e_1)=(1,0,0,0)^T=e_1\in \mathcal{X},T(e_2)=(1,1,0,0)^T=e_1+e_2\in \mathcal{X}$ ，故$\mathcal{X}$ 是 $T$ 的不变子空间。

**(b)** 由上一问知 $T(e_1)=e_1,T(e_2)=e_1+e_2$ ，故
$$
[T_{/\mathcal{X}}]_{e_1,e_2}=\left(
\begin{array}{rr}
1 & 1 \\
0 & 1
\end{array}
\right)
$$
**(c)** 因为 $\{e_1,e_2\}$ 是 $T$ 的不变子空间，所以任何由 $\{e_1,e_2\}$ 扩展得到的基 $\mathcal{B}=\{e_1,e_2,\alpha,\beta\}$， $T$ 在这组基下的矩阵表示 $[T]_{\mathcal{B}}$ 必然是一个准三角形矩阵
$$
\left(
\begin{array}{rrrr}
1 & 1 & a_{13} & a_{14} \\
0 & 1 & a_{23} & a_{24} \\
0 & 0 & a_{33} & a_{34} \\
0 & 0 & a_{43} & a_{44} \\
\end{array}
\right)
$$
