### 문제 1: 1차원 배열 두 개 행으로 연결 !!
#   두 개의 1차원 배열을 연결하세요.
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.concatenate((a,b), axis=0)
# 풀이
# array([1, 2, 3, 4, 5, 6])
pass

### 문제 2: 2차원 배열 두 개를 행으로 연결
#   두 개의 2차원 배열이 주어졌을 때, 이를 행(axis 0)을 따라 연결하세요.
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

np.concatenate((a,b), axis=0)
# 풀이
# array([[1, 2],
#        [3, 4],
#        [5, 6],
#        [7, 8]])
pass

### 문제 3: 2차원 배열 두 개를 열로 연결
#   두 개의 2차원 배열이 주어졌을 때, 이를 열(axis 1)을 따라 연결하세요.
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

np.concatenate((a,b), axis=1)
# 풀이
# array([[1, 2, 5, 6],
#        [3, 4, 7, 8]])
pass

### 문제 4: 다른 차원의 배열을 np.newaxis를 사용하여 연결
#   1차원 배열과 2차원 배열이 주어졌을 때, `np.newaxis`를 사용하여 1차원 배열을 수정한 후, 2차원 배열과 새로운 축을 따라 연결하세요.
a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])

a_newaxis = a[np.newaxis]
np.concatenate((a_newaxis, b), axis=0)
# 풀이
# np.concatenate((a_newaxis, b), axis=0)
pass

### 문제 5: 혼합 차원의 세 배열 연결
#   1차원 배열 두 개와 2차원 배열 하나가 주어졌을 때, 모든 배열을 연결하세요. 두 1차원 배열은 연결 전에 행으로 처리되어야 합니다.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([[7, 8, 9], [10, 11, 12]])

a_newaxis = a[np.newaxis]
b_newaxis = b[np.newaxis]
np.concatenate((a_newaxis, b_newaxis, c), axis=0)
# 풀이
# array([[ 1,  2,  3],
#        [ 4,  5,  6],
#        [ 7,  8,  9],
#        [10, 11, 12]])
pass