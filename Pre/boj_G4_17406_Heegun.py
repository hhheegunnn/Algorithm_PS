"""https://www.acmicpc.net/problem/17406"""


"""배열 돌리기4"""

# git add boj_implementation/G/G4/17406/boj_G4_17406_Heegun.py
# git commit -m "[김희건] boj 배열 돌리기 4"

from collections import deque
from itertools import permutations
from copy import deepcopy



def processing(r,c,s):

    while s > 0:

        sr = r-s
        sc = c-s

        er = r+s
        ec = c+s

        u_list = array[sr][sc:ec]
        r_list = deque()
        for i in range(sr,er):
            r_list.append(array[i][ec])
        d_list = array[er][sc+1:ec+1]
        l_list = deque()
        for i in range(sr+1,er+1):
            l_list.append(array[i][sc])

        array[sr][sc+1:ec+1] = u_list
        array[er][sc:ec] = d_list

        for i in range(sr+1,er+1):
            array[i][ec] = r_list.popleft()
        
        for i in range(sr,er):
            array[i][sc] = l_list.popleft()

        s -= 1

        
def find_result():
    min_list = []
    for a in array:
        min_list.append(sum(a))

    return min(min_list)



N, M, K = map(int,input().split())


n_array = [list(map(int,input().split())) for _ in range(N)]

K_list = [list(map(int,input().split())) for _ in range(K)]

K_list = list(permutations(K_list,K))

result = []

for i in K_list:
    array = deepcopy(n_array)
    for R,C,S in i:
        processing(R-1,C-1,S)

    result.append(find_result())

#print(result)
print(min(result))

"""
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
"""