###### Yuhang Liang 2020/12/18

### 程序文档
**data 文件夹**：存放矩阵数据的 txt 文件

**model 文件夹**：
所有的模型文件都在 model 文件夹中，每个分解算法都可以单独测试其正确性；

**utils 文件夹**：存放辅助功能实现文件，如格式化输出矩阵，计算矩阵的秩；

**main.py**：是模型使用的核心文件，可以调用关于矩阵分解的LU、QR(Gram-Schmidt)、
Orthogonal Reduction(Householder reduction和Givens reduction)
和URV的程序实现。具体方式如下：

```python
python main.py --model LU --input ./data/LU.txt
```
其中：

- `--model` 参数需要传入要调用的矩阵分解方法，可选项为 `[LU,QR,HR,GR,URV]` ，
  不传入参数则默认是`LU`分解。

- `--input` 参数需要传入矩阵 txt 文件所在路径，不传入路径则默认路径为`./data/LU.txt`。

