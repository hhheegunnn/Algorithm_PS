"""https://www.acmicpc.net/problem/2110"""



""" 공유기 설치 """

# git add week_07/Re_boj_S1_2110_Heegun.py
# git commit -m "[김희건] boj 공유기 설치"



n , c = map(int,input().split())

house = list(int(input()) for _ in range(n))

house.sort()

start = 1
end = house[-1] - house[0]


result = 0

while start <= end:
    gap = (start + end) //2

    h = house[0]
    cnt = 1

    for i in range(1,n):
        if house[i] >= h + gap:
            h = house[i]
            cnt += 1
    if cnt >= c:
        start = gap +1
        result = gap
    else:
        end = gap -1

print(result)
