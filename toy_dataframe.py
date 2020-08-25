#!/usr/bin/env python3

import pandas as pd
import numpy as np

A = np.array(['opencl', 'opencl', 'opencl', 'cpu', 'cpu', 'cpu'])
B = np.array(['f1', 'f2', 'f3']*2)
#C = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
#df = pd.DataFrame(data=C.T, columns=pd.MultiIndex.from_tuples(zip(A, B)))
df = pd.DataFrame(columns=pd.MultiIndex.from_tuples(zip(A, B)))
#df.index = ['file1', 'file2']

df.loc[0, ('opencl', 'f2')] = 5
df.loc[1, ('cpu', 'f3')] = 2
df.index = ['file1', 'file2']

print(df)
