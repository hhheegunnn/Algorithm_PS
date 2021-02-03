"""https://www.acmicpc.net/problem/4307"""


"""개미"""

# git add boj_implementation/S/S2/4307/Re_boj_S2_4307_Heegun.py
# git commit -m "[김희건] boj 개미 [ad hoc : 특별한 알고리즘을 사용하지 않고, 창의적인 아이디어를 이용하여 푸는 문제]"

import sys

input= sys.stdin.readline

T = int(input())


for _ in range(T):

    l, ant_num = map(int,input().rstrip().split())

    ant_list = []

    min_time = 0
    max_time = 0

    for _ in range(ant_num):
        ant = int(input().rstrip())
        if ant > l-ant:
            if min_time < l-ant:
                min_time = l-ant
            if max_time < ant:
                max_time = ant

        else:
            if min_time < ant:
                min_time = ant
            if max_time < l-ant:
                max_time = l-ant
        
    print(min_time, max_time)











    