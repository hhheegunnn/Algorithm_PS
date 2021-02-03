"""https://www.acmicpc.net/problem/11053"""


""" 가장 긴 증가하는 부분 수열"""

# git add week_08/boj_S2_11053_Heegun.py
# git commit -m "[김희건] boj 가장 긴 증가하는 부분 수열"


n = int(input())

num_list = list(map(int,input().split()))


dp = []

dp.append(1)
#dp.append(2 if num_list[0]<num_list[1] else 1)

for i in range(1,n):
    now = num_list[i]
    tmp = []
    for j in range(len(dp)):
        if num_list[j] < now:
            tmp.append(dp[j]+1)
        else:
            tmp.append(1)
    dp.append(max(tmp))

print(max(dp))

"""
num = int(input())

arr = list(map(int,input().split()))

dp = [1 for i in range(num)]

for i in range(1,num):
    for j in range(i):
        if (arr[i] > arr[j]) and (dp[j]+1 > dp[i]):
            dp[i] = dp[j]+1

print(max(dp))
"""
