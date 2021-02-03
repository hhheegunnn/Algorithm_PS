"""https://www.acmicpc.net/problem/1931"""


"""회의실배정"""


N = int(input())

time_list = []

for _ in range(N):
    s , e = map(int,input().split())

    time_list.append((s,e))

time_list.sort(key=lambda x: x[0]) #1,2 -> 2,2 -> 2,3
time_list.sort(key=lambda x: x[1])

result = [time_list[0]]

for i in range(1,len(time_list)):
    if time_list[i][0] >= result[-1][1]:
        result.append(time_list[i])
    else:
        continue
    

print(len(result))