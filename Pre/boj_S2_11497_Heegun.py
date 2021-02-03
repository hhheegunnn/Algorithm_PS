"""https://www.acmicpc.net/problem/11497"""


"""통나무 건너뛰기"""

# git add week_06/boj_S2_11497_Heegun.py
# git commit -m "[김희건] boj 통나무 건너뛰기"

from collections import deque

T = int(input())


for _ in range(T):

    N = int(input())

    tree = list(map(int,input().split()))

    tree.sort()

    #print(tree)

    result = deque([max(tree)])

    for i in range(N-2,-1,-1):
        if i%2 == 0:
            result.appendleft(tree[i])
        else:
            result.append(tree[i])

    max_diff = 0
    for i in range(N-1):
        max_diff = max(abs(result[i+1]-result[i]), max_diff)

    print(max_diff)

        



    

    