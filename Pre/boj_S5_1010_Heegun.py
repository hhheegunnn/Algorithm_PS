"""https://www.acmicpc.net/problem/1010"""



"""다리 놓기"""


T = int(input())



for _ in range(T):

    n,m = map(int,input().split())

    result = 1
    tmp = 1

    for i in range(n):
        result *= (m-i)
        tmp *= (i+1)

    print(result//tmp)








