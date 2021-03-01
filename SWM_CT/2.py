p,n,h = map(int,input().split())



time_table = [[] for _ in range(p+1)]

dp = [[0 for _ in range(25)] for _ in range(105)]
for i in range(1,p+1):
    dp[i][0] = 1

for _ in range(n):
    x,y = map(int,input().split())

    for i in range(h,y-1,-1):
        dp[x][i] 



"""
2 7 4
1 10
1 5
1 7
2 10
2 1
2 3
2 7
"""
 