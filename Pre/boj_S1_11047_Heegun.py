"""https://www.acmicpc.net/problem/11047"""


"""동전0"""

N,K = map(int,input().split())

coin_list = []
result = 0

for _ in range(N):
    coin_list.append(int(input()))


coin_list.sort(reverse = True)

for i in coin_list:
    if i > K:
        continue

    else:
        
        tmp = K//i
        result += tmp
        K -= i*tmp

print(result)
