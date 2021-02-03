"""https://www.acmicpc.net/problem/2812"""


"""크게 만들기"""



N,K = map(int,input().split())

num = input()

num = list(i for i in num)

cnt = 0

result =[]


for n in num:
    while result and result[-1] < n and K > 0:
        result.pop()
        K -= 1
    result.append(n)


if K != 0:

    result = result[:-K]


    


print(''.join(result))




