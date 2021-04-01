"""https://www.acmicpc.net/problem/13458"""

"""시험감독"""

from math import ceil

########### INPUT ############
N = int(input())


# A - 시험장당 응시 인원
A = list(map(int,input().split()))

# B - 총감독 감시 인원
# C - 부감독 감시 인원
B, C = map(int,input().split())

###############################


def solution():

    # 총 감독은 무조건 강의실마다 1 필요
    answer = N

    for i in range(N):
        A[i] -= B
        if A[i] > 0:
            answer += ceil(A[i]/C)
        
        else:
            continue

    return answer


print(solution())

