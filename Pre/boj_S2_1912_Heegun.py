"""https://www.acmicpc.net/problem/1912"""



"""연속합"""

# git add week_09_10/boj_S2_1912_Heegun.py
# git commit -m "[김희건] boj 연속합"


def solution(n_list,dp):

    max_sum = dp[0]

    for i in range(1,len(n_list)):
        
        k = max(dp[i-1] + n_list[i], n_list[i])
        dp.append(k)

        max_sum = max(max_sum, dp[i])


    return max_sum





N = int(input())
N_list = list(map(int,input().split()))
DP = [N_list[0]]
print(solution(N_list,DP))

