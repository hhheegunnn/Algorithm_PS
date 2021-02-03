"""https://www.acmicpc.net/problem/11399"""

"""ATM"""


N = int(input())

t_list = list(map(int,input().split()))

t_list.sort()

result = 0

for i in range(len(t_list)):
    result += sum(t_list[0:i+1])

print(result)