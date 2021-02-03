"""https://www.acmicpc.net/problem/1789"""


""" 수들의 합 """

# git add week_07/boj_S5_1789_Heegun.py

# git commit -m "[김희건] boj 수들의 합 [이분탐색 풀이법 확인]"


"""
s = int(input())

i = 1
answer = 0

while True:
    s -= i
    if s >=0:
        answer += 1
        i += 1

    else:
        print(answer)
        break
"""

### 이분 탐색  풀이
n = int(input())

answer = 0

left = 1

right = n


# 왼쪽이 오른쪽보다 커질때 까지 반복
while left <= right:
    mid = (left + right) // 2
    # 1 부터 mid까지의 합이 n보다 작거나 같으면 answer값을 mid로 갱신
    # 이후에 left값을 mid+1값으로 갱신
    if mid*(mid+1)//2 <=n :
        answer = mid
        left = mid + 1
    # 1 부터 mid까지의 합이 n보다 크다면 right 값을 mid-1로 갱신
    else:
        right = mid -1

print(answer)

