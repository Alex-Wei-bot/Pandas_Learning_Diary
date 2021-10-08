#矩阵乘法
from numpy.core.fromnumeric import shape
import pandas as pd
import numpy as np
M1=np.random.rand(2,3)
M2=np.random.rand(3,4)
res=np.empty((M1.shape[0],M2.shape[1]))
res = [[sum([M1[i][k] * M2[k][j] for k in range(M1.shape[1])]) for j in range(M2.
shape[1])] for i in range(M1.shape[0])]
print(((M1@M2) < 1e-15).all())