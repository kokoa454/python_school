import numpy as np

def get_around(ary, idx):
    firstIdx = idx[0]
    lastIdx = idx[1]
    aryLen = ary.shape[0]

    if firstIdx < 0 or firstIdx >= aryLen or lastIdx < 0 or lastIdx >= aryLen:
        return "エラー"
    else:
        return ary[max(0, firstIdx-1):min(aryLen, firstIdx+2), max(0, lastIdx-1):min(aryLen, lastIdx+2)]

# 実行例
N = 4
ary = np.arange(1, N*N+1).reshape(N,N)
print(ary)
print("\n")
"""
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]]
"""
idx = (0,0)  # ary[0,0] は 1
print(get_around(ary, idx))
print("\n")
"""
[[1 2]
 [5 6]]
"""
idx = (1,0)  # ary[1,0] は 5
print(get_around(ary, idx))
print("\n")
"""
[[ 1  2]
 [ 5  6]
 [ 9 10]]
"""
idx = (1,2)  # ary[1,2] は 7
print(get_around(ary, idx))
print("\n")
"""
[[ 2  3  4]
 [ 6  7  8]
 [10 11 12]]
"""

N = 5
ary = np.arange(3, N*N+3).reshape(N,N)
print(ary)
print("\n")
"""
[[ 3  4  5  6  7]
 [ 8  9 10 11 12]
 [13 14 15 16 17]
 [18 19 20 21 22]
 [23 24 25 26 27]]
"""
idx = (0,0)  # ary[0,0] は 3
print(get_around(ary, idx))
print("\n")
"""
[[3 4]
 [8 9]]
"""
idx = (2,1)  # ary[2,1] は 14
print(get_around(ary, idx))
print("\n")
"""
[[ 8  9 10]
 [13 14 15]
 [18 19 20]]
"""
idx = (3,4)  # ary[3,4] は 22
print(get_around(ary, idx))
print("\n")
"""
[[16 17]
 [21 22]
 [26 27]]
"""
idx = (4,4)  # ary[4,4] は 27
print(get_around(ary, idx))
print("\n")
"""
[[21 22]
 [26 27]]
"""