"""https://www.acmicpc.net/problem/17281"""


"""야구공 """

# git add boj_implementation/G/G4/17281/boj_G4_17281_Heegun.py
# git commit -m "[김희건] boj 야구 [시간초과 조건 빡쌔게]"

from itertools import permutations
import sys

input = sys.stdin.readline

Max_score = -1




def solution(p_seq):

    Score = 0
    pi = 0
    
    # 이닝별 점수 계산
    for ining in array:
        b1,b2,b3 = 0,0,0
        out_cnt = 0

        while True:

            # 3아웃 이닝 종료
            if out_cnt == 3:
                break
            """
            #h = array[ining][p_seq[pi]]
            if ining[p_seq[pi]] == 0:
                out_cnt += 1
            elif ining[p_seq[pi]] == 1:
                Score += b3
                b1,b2,b3 = 1,b1,b2
            elif ining[p_seq[pi]] == 2:
                Score += (b3+b2)
                b1,b2,b3 = 0,1,b1
            elif ining[p_seq[pi]] == 3:
                Score += (b1+b2+b3)
                b1,b2,b3 = 0,0,1
            elif ining[p_seq[pi]] == 4:
                Score += (b1+b2+b3 + 1)
                b1,b2,b3 = 0,0,0

            """
            if ining[p_seq[pi]] == 0:
                out_cnt += 1
            else:
                s,b1,b2,b3 = move(ining[p_seq[pi]],b1,b2,b3)
                Score += s
            pi += 1
            pi = pi%9
            
    return Score




def move(hit,b1,b2,b3):
    s = 0

    if hit == 1:
        s += b3
        b1,b2,b3 = 1,b1,b2

    elif hit == 2:
        s += (b3+b2)
        b1,b2,b3 = 0,1,b1


    elif hit == 3:
        s += (b1+b2+b3)
        b1,b2,b3 = 0,0,1


    elif hit == 4:
        s += (b1+b2+b3 + 1)
        b1,b2,b3 = 0,0,0


    return s, b1,b2,b3

            



N = int(input())

array = [list(map(int,input().split())) for _ in range(N)]

p_num = [i for i in range(9)]

tmp = list(permutations(p_num[1:],8))



for i in range(len(tmp)):
    k = []
    a = list(tmp[i])
    k += a[0:3]
    k.append(0)
    k += a[3:]

    Max_score = max(Max_score, solution(k))



print(Max_score)






