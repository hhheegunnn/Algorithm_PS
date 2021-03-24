"""https://www.acmicpc.net/problem/2407"""


"""조합"""



N,M = map(int,input().split())


a = 1

for i in range(M):
    
    a = a*(N-i)//(i+1)

print(a)