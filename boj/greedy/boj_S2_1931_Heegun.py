"""https://www.acmicpc.net/problem/1931"""

""" 회의실 배정 """

N = int(input())
time_table = []

for _ in range(N):
    s,e = map(int,input().split())
    time_table.append([s,e])

time_table.sort(key=lambda x: (x[1],x[0]))


cnt = 0
e_time = 0

for m in time_table:
    if e_time <= m[0]:
        cnt += 1
        e_time = m[1]

print(cnt)


