#卡方统计量
import numpy as np
np.random.seed(0)
A=np.random.randint(10,20,(8,5))
B=np.empty((8,5))
x=0
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        B[i][j]=A.sum(0)[j]*A.sum(1)[i]/A.sum()
        x=(A[i][j]-B[i][j])**2/B[i][j]
print(f'{x**2:.20}')