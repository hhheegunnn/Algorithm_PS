"""https://www.acmicpc.net/problem/13549"""


"""숨바꼭질3"""

# git add week_11/Re_boj_G5_13549_Heegun.py
# git commit -m "[김희건] boj 숨바꼭질3 [거의 bfs, 약간 다익스트라?]"

from collections import deque


def solution(start,end):
    q = deque([start])
    distance[start] = 0

    while q:


        now = q.popleft()

        if now == end:
            return distance[end]



        A = now - 1
        if A >= 0:
            if distance[A] == -1:
                distance[A] = distance[now]+ 1
                q.append(A)
            else:
                if distance[A] > distance[now] + 1:
                    distance[A] = distance[now]+1
                    q.append(A)

        B = now + 1
        if B < 100001:
            if distance[B] == -1:
                distance[B] = distance[now] + 1
                q.append(B)
            else:
                if distance[B] > distance[now] + 1:
                    distance[B] = distance[now]+1
                    q.append(B)

        C = now * 2
        if C < 100001:
            if distance[C] == -1:
                distance[C] = distance[now]
                q.append(C)
            else:
                if distance[C] > distance[now]:
                    distance[C] = distance[now]
                    q.append(C)









N,K = map(int,input().split())
distance = [-1] * 100001


print(solution(N,K))

