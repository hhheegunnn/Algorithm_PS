"""https://www.acmicpc.net/problem/11722"""


""" 가장 긴 감소하는 부분 수열"""

# git add week_09_10/boj_S2_11722_Heegun.py
# git commit -m "[김희건] boj 가장 긴 감소하는 부분 수열"

def solution(n_list,dp):

    for i in range(len(n_list)):
       
        for j in range(i-1,-1,-1):
            if n_list[i] < n_list[j]:
                if 1+dp[j] > dp[i]:
                    dp[i] = 1+dp[j]

    return max(dp)






N = int(input())
N_list = list(map(int,input().split()))
DP = [1 for _ in range(N)]
print(solution(N_list,DP))