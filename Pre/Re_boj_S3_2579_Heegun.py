"""https://www.acmicpc.net/problem/2579"""


"""계단 오르기 """

# git add week_08/Re_boj_S3_2579_Heegun.py
# git commit -m "[김희건] boj 계단 오르기"

num = int(input())

arr = [0 for i in range(300)]

for i in range(num):
    arr[i] = int(input())

dp = [0 for i in range(300)]
dp[0] = arr[0]
dp[1] = max(arr[0]+arr[1],arr[1])
dp[2] = max(arr[0]+arr[2],arr[1]+arr[2])

for n in range(3,num):
    dp[n] = max(dp[n-3]+arr[n-1]+arr[n],dp[n-2]+arr[n])

print(dp[num-1])





















