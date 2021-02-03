"""https://www.acmicpc.net/problem/14501"""


""" 퇴사 """

# git add week_09/Re_boj_S4_14501_Heegun.py
# git commit -m "[김희건] boj 퇴사"


n = int(input())

table = [list(map(int,input().split())) for _ in range(n)]


dp = [0]*25

"""
for i in range(n-1,-1,-1):
    if table[i][0]+i >= n:
        table[i][1] = 0
"""
print(table)

"""
for i in range(n):

    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]
    
    if dp[i + table[i][0]] < dp[i] + table[i][1]:
        dp[i + table[i][0]] = dp[i] + table[i][1]
"""

max_p = 0
for i in range(n):
    max_p = max(max_p,dp[i])
    if i + table[i][0] > n:
        continue
    dp[i+table[i][0]] = max(max_p+table[i][1], dp[i+table[i][0]])

print(dp)











