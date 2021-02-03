"""https://www.acmicpc.net/problem/17779"""


""" 게리맨더링 2 """

# git add boj_implementation/G/G4/17779/Re_boj_G4_17779_Heegun.py
# git commit -m "[김희건] boj 게리맨더링2 [깡구현]"


## 1번 구역 합 구하기 
def sum_1D(graph, x, y, d1, d2):
    sum_1 = 0
    for i in range(0, x+d1):
        for j in range(0, y+1):
            sum_1 = sum_1 + graph[i][j]
    #5구역에 해당하는 곳 제외
    t = -1
    for i in range(x, x+d1):
        t = t+1
        for j in range(y-t,y+1):
            sum_1 = sum_1 - graph[i][j]
    return sum_1

## 2번 구역 합 구하기
def sum_2D(graph, x, y, d1, d2):
    sum_2 = 0
    for i in range(0, x+d2+1):
        for j in range(y+1, N):
            sum_2 = sum_2 + graph[i][j]
    #5구역에 해당하는 곳 제외
    t = 0
    for i in range(x+1, x+d2+1):
        t = t+1
        for j in range(y+1, y+1+t):
            sum_2 = sum_2 - graph[i][j]
    return sum_2



def sum_3D(graph, x, y, d1, d2):
    sum_3 = 0
    for i in range(x+d1, N):
        for j in range(0, y-d1+d2):
            sum_3 = sum_3 + graph[i][j]
    #5구역 제외
    t = -1
    for i in range(x+d1, x+d1+d2+1):
        t = t+1
        for j in range(y-d1+t, y-d1+d2):
            sum_3 = sum_3 - graph[i][j]
    return sum_3

## 4번 구역 합 구하기
def sum_4D(graph, x, y, d1, d2):
    sum_4 = 0
    for i in range(x+d2+1,N):
        for j in range(y-d1+d2, N):
            sum_4 = sum_4 + graph[i][j]
    #5구역 제외
    t = -1
    for i in range(x+d2+1, x+d2+d1+1):
        t = t+1
        for j in range(y-d1+d2, y+d2-t):
            sum_4 = sum_4 - graph[i][j]
    return sum_4





N = int(input())


dt_map = [list(map(int,input().split())) for _ in range(N)]


total_sum = 0
for i in range(N):
    total_sum = total_sum + sum(dt_map[i])

minvalue = float('inf') # 최솟값 = 인구가 가장 많은 선거구 - 가장 적은 선거구
for x in range(N):
    for y in range(N):
        for d1 in range(1, y+1):
            for d2 in range(1, N+1):
                if (0 <= x+d1 < N and 0 <= y-d1 < N) and (0 <= x+d2 < N and 0 <= y+d2 < N) and (0 <= x+d1+d2 < N and 0 <= y-d1+d2 < N):
                    district = []
                    district.append(sum_1D(dt_map, x, y, d1, d2)) #1번구역
                    district.append(sum_2D(dt_map, x, y, d1, d2)) #2번구역
                    district.append(sum_3D(dt_map, x, y, d1, d2)) #3번구역
                    district.append(sum_4D(dt_map, x, y, d1, d2)) #4번구역
                    district.append(total_sum - sum(district)) #5번구역
                    district.sort() #값이 5개밖에 안되므로 정렬해주자
                    if minvalue > district[-1]-district[0]:
                        minvalue = district[-1]-district[0]

print(minvalue)


