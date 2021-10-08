#更新矩阵
import numpy as np
m=int(input())
n=int(input())
A=np.random.rand(m,n)
B=np.empty((m,n))
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        sum=0
        for k in range(A.shape[1]):
            sum+=A[i][k]**-1
        B[i][j]=A[i][j]*sum
print(A)
print(B)
