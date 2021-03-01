# 슬라이딩 윈도우

import sys

n , m, e = map(int,input().split())

p_list = list(map(int,input().split()))


l = 0
r = m-1 
ans = sys.maxsize

def solution(l,r):
    return max(e, p_list[r]) - min(e, p_list[l])

while r < n:
    ans = min(ans,solution(l,r))

    l+=1
    r+=1


print(ans)




"""
6 3 7
2 4 5 8 11 12
"""