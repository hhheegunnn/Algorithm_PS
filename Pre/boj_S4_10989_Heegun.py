"""https://www.acmicpc.net/problem/10989"""


"""수 정렬하기 3"""

# git add week_06/boj_S4_10989_Heegun.py
# git commit -m "[김희건] boj 수 정렬하기3 [계수정렬]"

import sys
input = sys.stdin.readline

N = int(input())
#result = [int(input()) for _ in range(N)]
arr = [0]*10001

def counting_sort():
    
    for i in range(N):
        tmp = int(input())
        arr[tmp] += 1
    
    for i in range(len(arr)):
        if arr[i] != 0:
            while True:
                if arr[i] == 0:
                    break
                else:
                    print(i)
                    arr[i] -= 1


    
# 계수정렬 메모리 초과
counting_sort()

"""
for i in result:
    print(i)
"""