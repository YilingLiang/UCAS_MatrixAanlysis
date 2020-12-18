### 矩阵分析第七次作业

#### 课件8 Exercises 1

**解： ** **Household reduction：** 

设 
$$
A=\left(
\begin{array}{rrr}
1 & 19 & -34\\
-2 & -5 & 20\\
2 & 8 & 37
\end{array}
\right)=(A_{*1},A_{*2},A_{*3})
$$
取 $u_1=A_{*1}-||A_{*1}||e_1=(-2,-2,2)^T$，于是令
$$
R_1=I-2\frac{u_1u_1^T}{u_1^Tu_1}=\left(
\begin{array}{rrr}
1/3 & -2/3 & 2/3\\
-2/3 & 1/3 & 2/3\\
2/3 & 2/3 & 1/3
\end{array}
\right)
$$
此时
$$
R_1A=\left(
\begin{array}{rrr}
3 & 15 & 0\\
0 & -9 & 54\\
0 & 12 & 3
\end{array}
\right)=\left(
\begin{array}{rr}
3 & \beta^T\\
\alpha & B 
\end{array}
\right)
$$
取 $u_2=B_{*1}-||B_{*1}||e_1=(-24,12)^T$，于是得
$$
\hat{R}_2=I-2\frac{u_2u_2^T}{u_2^Tu_2}=\left(
\begin{array}{rrr}
-3/5 & 4/5\\
4/5 & 3/5\\
\end{array}
\right)
$$
令
$$
R_2=\left(
\begin{array}{rrr}
1 & \mathbf{0}^T\\
\mathbf{0} & \hat{R}_2\\
\end{array}
\right)=\left(
\begin{array}{rrr}
1 & 0 & 0\\
0 & -3/5 & 4/5\\
0 & 4/5 & 3/5\\
\end{array}
\right)
$$
于是有
$$
R_2R_1A=\left(
\begin{array}{rrr}
3 & 15 & 0\\
0 & 15 & -30\\
0 & 0 & 45\\
\end{array}
\right)=\boxed{R}
$$
由于 $R_1,R_2$ 都是正交矩阵，故 $R_2R_1$ 也为正交矩阵，所以 $(R_2R_1)^{-1}=(R_2R_1)^{T}$ ，于是得到
$$
A=(R_2R_1)^{T}R=QR
$$
其中
$$
\boxed{Q}=(R_2R_1)^{T}=\left(
\begin{array}{rrr}
1/3 & 14/15 & -2/15\\
-2/3 & 1/3 & 2/3\\
2/3 & -2/15 & 11/15\\
\end{array}
\right)
$$
**Givens reduction：** 

令
$$
P_{12}=\left(
\begin{array}{rrr}
1/\sqrt{5} & -2/\sqrt{5} & 0\\
2/\sqrt{5} & 1/\sqrt{5} & 0\\
0 & 0 & 1\\
\end{array}
\right),\quad then\ P_{12}A=\left(
\begin{array}{rrr}
\sqrt{5} & 29/\sqrt{5} & -74/\sqrt{5}\\
0 & 33/\sqrt{5} & -48/\sqrt{5}\\
2 & 8 & 37\\
\end{array}
\right)
$$
令
$$
P_{13}=\left(
\begin{array}{rrr}
\sqrt{5}/3 & 0 & 2/3\\
0 & 1 & 0\\
-2/3 & 0 & \sqrt{5}/3\\
\end{array}
\right),\quad then\ P_{13}P_{12}A=\left(
\begin{array}{rrr}
3 & 15 & 0\\
0 & 33/\sqrt{5} & -48/\sqrt{5}\\
0 & -6/\sqrt{5} & 111/\sqrt{5}\\
\end{array}
\right)
$$
令
$$
P_{23}=\left(
\begin{array}{rrr}
1 & 0 & 0\\
0 & 11/5\sqrt{5} & -2/5\sqrt{5}\\
0 & 2/5\sqrt{5} & 11/5\sqrt{5}\\
\end{array}
\right),\quad then\ P_{23}P_{13}P_{12}A=\left(
\begin{array}{rrr}
3 & 15 & 0\\
0 & 15 & 30\\
0 & 0 & 45\\
\end{array}
\right)=\boxed{R}
$$
故
$$
A=(P_{23}P_{13}P_{12})^{T}R=QR
$$

#### 课件8 Exercises 2

**解：** 取 $u_1=A_{*1}-||A_{*1}||e_1=(-1,2,-2,1)^T$ ，令
$$
R_1=I-2\frac{u_1u_1^T}{u_1^Tu_1}=\left(
\begin{array}{rrr}
4/5 & 2/5 & -2/5 & 1/5\\
2/5 & 1/5 & 4/5 & -2/5\\
-2/5 & 4/5 & 1/5 & 2/5\\
1/5 & -2/5 & 2/5 & 4/5\\
\end{array}
\right)
$$
于是
$$
R_1A=\left(
\begin{array}{rrr}
5 & -15 & 5 \\
0 & 10 & -5 \\
0 & -10 & 2 \\
0 & 5 & 14 \\
\end{array}
\right)
$$
取 $u_2=(10,-10,5)^T-(15,0,0)^T=(-5,-10,5)^T$ ，令
$$
\hat{R}_2=I-2\frac{u_2u_2^T}{u_2^Tu_2}=\left(
\begin{array}{rrr}
2/3 & -2/3 & 1/3\\
-2/3 & -1/3 & 2/3\\
1/3 & 2/3 & 2/3
\end{array}
\right),R_2=\left(
\begin{array}{rrr}
1 & 0 & 0 & 0 \\
0 & 2/3 & -2/3 & 1/3\\
0 & -2/3 & -1/3 & 2/3\\
0 & 1/3 & 2/3 & 2/3
\end{array}
\right)
$$
于是
$$
R_2R_1A=\left(
\begin{array}{rrr}
5 & -15 & 5 \\
0 & 15 & 0 \\
0 & 0 & 12 \\
0 & 0 & 9 \\
\end{array}
\right)
$$
取 $u_3=(12,9)^T-(15,0)^T=(-3,9)^T$ ，令
$$
\hat{R}_3=I-2\frac{u_3u_3^T}{u_3^Tu_3}=\left(
\begin{array}{rr}
4/5 & 3/5\\
3/5 & -4/5\\
\end{array}
\right),R_3=\left(
\begin{array}{rrr}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0\\
0 & 0 & 4/5 & 3/5\\
0 & 0 & 3/5 & -4/5
\end{array}
\right)
$$
 于是
$$
R_3R_2R_1A=\left(
\begin{array}{rrr}
5 & -15 & 5 \\
0 & 15 & 0 \\
0 & 0 & 15 \\
0 & 0 & 0 \\
\end{array}
\right)=R
$$
则有
$$
A=(R_3R_2R_1)^{-1}R=(R_3R_2R_1)^{T}R=R_1R_2R_3R
$$
其中
$$
R_1R_2R_3=\frac{1}{15}\left(
\begin{array}{rrr}
12 & 9 & 0 & 0 \\
6 & -8 & -5 & -10\\
-6 & 8 & 2 & -11\\
3 & -4 & 14 & -2
\end{array}
\right)
$$
上述矩阵的前 $3$ 列为 $R(A)$ 的一组标准正交基。

#### 课件8 Exercises 7

**解： (a)** $rank(\mathcal{B_X},\mathcal{B_Y})=3,rank(\mathcal{B_X})=2,rank(\mathcal{B_Y})=1$， 说明 $R^3=\mathcal{B_X}\oplus\mathcal{B_Y}$ ，故二者在 $R^3$ 互为补空间。

**(b)** 沿 $\mathcal{Y}$ 向 $\mathcal{X}$ 的投影矩阵为
$$
P=[X|0][X|Y]^{-1}=\left(
\begin{array}{rrr}
1 & 1 & -1  \\
0 & 3 & -2 \\
0 & 3 & -2  
\end{array}
\right)
$$
于是沿 $\mathcal{X}$  向 $\mathcal{Y}$ 投影矩阵为
$$
Q=I-P=\left(
\begin{array}{rrr}
0 & 1 & -1  \\
0 & 2 & -2 \\
0 & 3 & -3  
\end{array}
\right)
$$
**(c)** 只需计算
$$
Qv=(2,4,6)^T
$$
**(d)** $P,Q$ 都是投影矩阵，所以是幂等矩阵。计算性验证：
$$
P^2=\left(
\begin{array}{rrr}
1 & 1 & -1  \\
0 & 3 & -2 \\
0 & 3 & -2  
\end{array}
\right)\left(
\begin{array}{rrr}
1 & 1 & -1  \\
0 & 3 & -2 \\
0 & 3 & -2  
\end{array}
\right)=\left(
\begin{array}{rrr}
1 & 1 & -1  \\
0 & 3 & -2 \\
0 & 3 & -2  
\end{array}
\right)=P\\
Q^2=\left(
\begin{array}{rrr}
0 & 1 & -1  \\
0 & 2 & -2 \\
0 & 3 & -3  
\end{array}
\right)\left(
\begin{array}{rrr}
0 & 1 & -1  \\
0 & 2 & -2 \\
0 & 3 & -3  
\end{array}
\right)=\left(
\begin{array}{rrr}
0 & 1 & -1  \\
0 & 2 & -2 \\
0 & 3 & -3  
\end{array}
\right)=Q
$$
**(e)** 首先证明 $R(P)=\mathcal{X}$ ，$\mathcal{X}$ 的每个向量可由 $P$ 的列向量线性表出
$$
\mathcal{B_{X}}_1=\frac{1}{3}(2P_1+P_2),\mathcal{B_{X}}_2=2(P_2+P_3)+P_1,
$$
且两者秩相等，故它们张成的空间一样。即 $R(P)=\mathcal{X}$ 。

接下来证明 $N(Q)=\mathcal{X}$ ，解线性方程组 $Qx=0$ ，得基础解系 $\xi_1=(1,1,1)^T,\xi_2=(1,2,2)^T$ ，发现 $\mathcal{X}$ 恰好可作为基础解系，故  $N(Q)=\mathcal{X}$ 。

同理可证明 $R(Q)=\mathcal{Y},N(P)=\mathcal{Y}$ 。