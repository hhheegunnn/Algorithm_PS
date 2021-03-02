"""https://www.acmicpc.net/problem/2212"""


"""센서"""

N = int(input())

K = int(input())

sensor = list(map(int,input().split()))
sensor.sort()


if N <= K:
    print(0)

else:
    diff = []

    for i in range(N-1):
        diff.append(sensor[i+1] - sensor[i])
    diff.sort()

    for i in range(K-1):
        diff.pop()

    print(sum(diff))

