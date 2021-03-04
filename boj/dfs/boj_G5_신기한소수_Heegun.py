"""https://www.acmicpc.net/problem/2023"""


"""신기한 소수"""

from math import sqrt

N = int(input())

def check_prime(number):

    if number == 1:
        return False

    for i in range(2,int(sqrt(number))+1):

        if number%i == 0:
            return False

    return True

def dfs(stack,d):
    if d == 1:
        print(stack)
        return
    
    stack *= 10
    for i in range(10):
        if check_prime(stack+i):
            dfs(stack+i,d-1)


for i in [2,3,5,7]:
    dfs(i,N)




