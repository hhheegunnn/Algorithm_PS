"""https://www.acmicpc.net/problem/4307"""



"""개매"""

import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    l , n = map(int,input().rstrip().split())
    mn,mx = [],[]

    for _ in range(n):
        num = int(input())

        left = num
        right = l-num

        if left <= right:
            mx.append(right)
            mn.append(left)
        else:
            mx.append(left)
            mn.append(right)

    print(max(mn),max(mx))

