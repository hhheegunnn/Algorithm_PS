"""https://www.acmicpc.net/problem/1699"""


""" 제곱수의 합"""

# git add week_09/boj_S31699_Heegun.py
# git commit -m "[김희건] boj 제곱수의 합"



n = int(input())


dp = [0 for _ in range(n+1)]

for i in range(1,n+1):

    dp[i] = i

    for j in range(1,i):
        if j*j > i:
            break
        dp[i] = min(dp[i],dp[i-j*j] + 1)


print(dp[n])


         

