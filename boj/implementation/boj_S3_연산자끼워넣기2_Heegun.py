"""https://www.acmicpc.net/problem/15658"""


"""연산자끼워넣기2"""


import sys

N = int(input())
numbers = list(map(int,input().split()))
op = list(map(int,input().split()))
mx, mn = -sys.maxsize, sys.maxsize


def solution(index, ans, add, sub, mul, div):
    global mx,mn
    if index >=N :
        mx = max(mx,ans)
        mn = min(mn,ans)
        return
    
    if add:
        solution(index+1, ans+numbers[index], add-1, sub, mul, div)
    if sub:
        solution(index+1, ans-numbers[index], add, sub-1, mul, div)
    if mul:
        solution(index+1, ans*numbers[index], add, sub, mul-1, div)
    if div:
        solution(index+1, ans//numbers[index] if ans > 0 else -((-ans)//numbers[index]), add, sub, mul, div-1)

solution(1, numbers[0], op[0], op[1], op[2], op[3])
print(mx)
print(mn)

