### 矩阵分析第三次作业

#### 课件5 练习6

**证明：** 

考察线性方程组 $Ax=0$ 与 $A^TAx=0$ ，显然：
$$
\forall x,Ax=0 \Longrightarrow A^TAx=0
$$
这说明 $N(A)\subseteq N(A^TA)$ 。另外：
$$
\forall x, A^TAx=0 \Longrightarrow x^TA^TAx=(Ax)^2=0 \Longrightarrow Ax=0
$$
于是 $N(A^TA)\subseteq N(A)$ 。于是  $N(A^TA)= N(A)$ ，而对于 $Ax=0$ 解空间的维数有 $dim N(A)=n-rank(A)$ ， 两矩阵的列数一样，于是必有 $rank(A^TA)=rank(A)$ 。

另外：
$$
\forall x \in N(A^T)\cap R(A)\Longrightarrow A^Tx=0,Ay=0
$$
于是：
$$
y^TA^Tx=x^Tx=0\Longrightarrow x=0
$$
这说明 $dim (N(A) \cap R(A^T))=0$ 。

于是 $rank(AA^T)=rank(A^T)-dim(N(A)\cap R(A^T))=rank(A^T)$ 。

综上：$rank(A)=rank(A^T)=rank(AA^T)=rank(A^TA)$ 。

计算性证明：对 $A,A^TA,AA^T$ 进行初等变换求秩：
$$
A=\left(
\begin{array}{rrrr}
1 & 3 & 1 & -4 \\
-1 & -3 & 1 & 0 \\
2 & 6 & 2 & -8
\end{array}
\right) \longrightarrow
\left(
\begin{array}{rrrr}
1 & 3 & 1 & -4 \\
0 & 0 & 2 & -4 \\
0 & 0 & 0 & 0
\end{array}
\right),rank(A)=2
$$

$$
A^TA=\left(
\begin{array}{rrrr}
6 & 18 & 4 & -20 \\
18 & 54 & 12 & -60 \\
4 & 12 & 6 & -20 \\
-20 & -60 & -20 & 80
\end{array}
\right) \longrightarrow
\left(
\begin{array}{rrrr}
3 & 9 & 2 & -10 \\
3 & 9 & 2 & -10 \\
2 & 6 & 3 & -10 \\
-1 & -3 & -1 & 4
\end{array}
\right) \longrightarrow \\
\left(
\begin{array}{rrrr}
3 & 4 & 2 & 10 \\
0 & 0 & 0 & 0 \\
0 & 0 & 1 & -2 \\
0 & 0 & 0 & 0
\end{array}
\right)\longrightarrow
\left(
\begin{array}{rrrr}
3 & 4 & 2 & 10 \\
0 & 0 & 1 & -2 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{array}
\right),rank(A^TA)=2
$$

$$
AA^T=\left(
\begin{array}{rrr}
27 & -9 & 54  \\
-9 & 11 & -18 \\
54 & -18 & 108 
\end{array}
\right) \longrightarrow
\left(
\begin{array}{rrr}
3 & -1 & 6  \\
-9 & 11 & -18 \\
3 & -1 & 6 
\end{array}
\right) \longrightarrow
\left(
\begin{array}{rrr}
3 & -1 & 6  \\
0 & 8 & 0 \\
0 & 0 & 0 
\end{array}
\right),rank(AA^T)=2
$$

#### 课件5 练习 9

**解：** 使用最小二乘法（LSE），设 $\mathbf{x}_i=(1,x_i,x_i^2,...)^T$ ，$y_i=y_i$， $w=(\alpha_0,\alpha_1,\alpha_2,...)^T$ ，
$$
A=\left(
\begin{array}{rrrr}
1 & x_1 & x_1^2 & ...  \\
1 & x_2 & x_2^2 & ...  \\
... & ... & ... & ...
\end{array}
\right),A^T=
\left(
\begin{array}{rrrr}
\mathbf{x}_1 ,& \mathbf{x}_2 & ...
\end{array}
\right),\mathbf{b}=\left(
\begin{array}{r}
y_1  \\
y_2  \\
...
\end{array}
\right)
$$
如果使用 $y=w^T \mathbf{x}$ 对数据进行最小二乘拟合，即要求得参数 $w$ 使得误差最小，误差函数：
$$
L(w)=\sum\limits_{i=1}^N(w^Tx_i-y_i)^2
$$
对误差函数进行矩阵化：
$$
\begin{align}
L(w)&=(w^T\mathbf{x}_1-y_1,\cdots,w^T\mathbf{x}_N-y_N)\cdot (w^T\mathbf{x}_1-y_1,\cdots,w^T\mathbf{x}_N-y_N)^T\nonumber\\
&=(w^TA^T-\mathbf{b}^T)\cdot (Aw-\mathbf{b})=w^TA^TXw-Y^TAw-w^TA^TY+\mathbf{b}^T\mathbf{b}\nonumber\\
&=w^TA^TAw-2w^TA^T\mathbf{b}+\mathbf{b}^T\mathbf{b}
\end{align}
$$
最小化 $L$ 求得 $ \hat{w}$ ：
$$
\begin{align}
\hat{w}=\mathop{argmin}\limits_wL(w)&\longrightarrow\frac{\partial}{\partial w}L(w)=0\nonumber\\
&\longrightarrow2A^TA\hat{w}-2A^T\mathbf{b}=0\nonumber
\end{align}
$$
（如果 $A^TA$ 可逆的话， $\hat{w}=(A^TA)^{-1}A^T\mathbf{b}$）

对于本题，**情况1**，使用 $y=\alpha_0+\alpha_1x$ 进行拟合
$$
A=\left(
\begin{array}{rr}
1 & -5 \\
1 & -4  \\
1 & -3  \\
1 & -2  \\
1 & -1 \\
1 & 0  \\
1 & 1  \\
1 & 2  \\
1 & 3  \\
1 & 4  \\
1 & 5  \\
\end{array}
\right),A^TA=\left(
\begin{array}{rr}
11 & 0 \\
0 & 110  
\end{array}
\right)
$$
利用公式可以求得 $w=(\alpha_0,\alpha_1)^T=(\frac{106}{11}, \frac{2}{11})^T$ ，再带入误差公式 $=w^TA^TAw-2w^TA^T\mathbf{b}+\mathbf{b}^T\mathbf{b}$ ，得到误差为 $L(w)=162.9091$ 。

对于本题，**情况2**，使用 $y=\alpha_0+\alpha_1x+\alpha_2x^2$ 进行拟合
$$
A=\left(
\begin{array}{rrr}
1 & -5&25 \\
1 & -4&16  \\
1 & -3&9  \\
1 & -2&4  \\
1 & -1&1 \\
1 & 0&0  \\
1 & 1&1  \\
1 & 2&4  \\
1 & 3&9  \\
1 & 4&16  \\
1 & 5&25  \\
\end{array}
\right),A^TA=\left(
\begin{array}{rr}
11 & 0 & 110\\
0 & 110 & 0\\
110 & 0 & 1958\\
\end{array}
\right)
$$
利用公式可以求得 $w=(\alpha_0,\alpha_1,\alpha_2)^T=(\frac{1998}{143},\frac{2}{11},-\frac{62}{143})^T$ ，误差为 $L(w)=1.6224$ 。