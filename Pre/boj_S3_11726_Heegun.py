"""https://www.acmicpc.net/workbook/view/6141"""



# git add week_09_10/boj_S3_11726_Heegun.py
# git commit -m "[김희건] boj 2Xn 타일링"

"""2xn 타일링"""



def solution(n,dp):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    for i in range(3,n+1):
        dp.append(dp[i-1]+dp[i-2])

    return dp[n]





N = int(input())
DP = [0,1,2]

print(solution(N,DP)%10007)