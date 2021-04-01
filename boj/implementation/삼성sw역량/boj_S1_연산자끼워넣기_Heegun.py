"""https://www.acmicpc.net/problem/14888"""


"""연산자 끼워넣기"""

import sys


N = int(input())

num_list = list(map(int,input().split()))

op_list = list(map(int,input().split()))

mx = -sys.maxsize
mn = sys.maxsize


def solution(i, ans, add, sub, mul, div):
    global mx,mn

    if i == N:
        mx = max(mx,ans)
        mn = min(mn,ans)
        return

    else:
        if add:
            solution(i+1, ans + num_list[i], add-1,sub,mul,div )
        if sub:
            solution(i+1, ans - num_list[i], add,sub-1,mul,div )
        if mul:
            solution(i+1, ans * num_list[i], add,sub,mul-1,div )
        if div:
            solution(i+1,int(ans/num_list[i]), add,sub,mul,div-1)


solution(1,num_list[0], op_list[0], op_list[1], op_list[2], op_list[3])
print(mx)
print(mn)





