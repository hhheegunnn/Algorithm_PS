"""https://www.acmicpc.net/problem/9095"""


"""1,2,3 더하기"""

# git add week_09_10/boj_S3_9095_Heegun.py
# git commit -m "[김희건] boj 1,2,3더하기"


def solution(n):

    if n == 1:
        return 1

    for i in range(3,n):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])

    return dp[n-1]





for _ in range(int(input())):
    dp = [1,2,4]
    N = int(input())
    print(solution(N))