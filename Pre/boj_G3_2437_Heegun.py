"""https://www.acmicpc.net/problem/2437"""


"""저울"""


N = int(input())

w_list = list(map(int,input().split()))

w_list.sort()

w_sum = 0

for i in range(N):
    if w_sum + 1 >= w_list[i]:
        w_sum += w_list[i]
    else:
        break

print(w_sum+1)


