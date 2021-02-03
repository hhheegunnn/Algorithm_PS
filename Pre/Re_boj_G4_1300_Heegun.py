"""https://www.acmicpc.net/problem/1300"""


"""  k 번째 수 """

# git add week_07/Re_boj_G4_1300_Heegun.py
# git commit -m "[김희건] boj k번째 수"

from bisect import bisect_right, bisect_left

n = int(input())

k = int(input())


start = 1
#end = k
end = n*n

while start <= end:
    mid = (start + end) // 2

    tmp = 0

    for i in range(1,n+1):
        tmp += min(mid//i, n)

    if tmp >= k:
        result = mid
        end = mid -1 
    else:
        start = mid + 1

print(result)



