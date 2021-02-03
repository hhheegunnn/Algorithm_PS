"""https://www.acmicpc.net/problem/1149"""


""" RGB거리"""

# git add week_08/boj_S1_1149_Heegun.py
# git commit -m "[김희건] boj RGB거리"



n = int(input())

cost = []

for _ in range(n):
    cost.append(list(map(int,input().split())))



for i in range(1,n):
    cost[i][0] = min(cost[i-1][1],cost[i-1][2]) + cost[i][0]
    cost[i][1] = min(cost[i-1][0],cost[i-1][2]) + cost[i][1]
    cost[i][2] = min(cost[i-1][1],cost[i-1][0]) + cost[i][2]

print(min(cost[n-1]))

