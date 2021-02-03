"""https://www.acmicpc.net/problem/2193"""


"""이친수"""

# git add week_09_10/boj_S3_2193_Heegun.py
# git commit -m "[김희건] boj 이친수"



def solution(n,dp):

    if n == 1:
        return 1

    if n == 2:
        return 1

    else:
        for i in range(2,n):
            dp.append(dp[i-1] + dp[i-2])

    return dp[n-1]




N = int(input())
dp = [1,1]
print(solution(N,dp))