"""https://www.acmicpc.net/problem/14889"""


"""스타트와 링크"""


from itertools import combinations,permutations
import sys


#### INPUT ####
N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

###############

def solution():

    min_d = sys.maxsize

    team = list(combinations(range(N),N//2))

    for i in range(len(team)//2):

        t1_score = 0 
        t2_score = 0

        t1_list = team[i]
        t2_list = team[-1-i]

        for y,x in list(permutations(t1_list,2)):
            t1_score += board[y][x]

        for y,x in list(permutations(t2_list,2)):
            t2_score += board[y][x]


        min_d = min(min_d, abs(t1_score-t2_score))

    return min_d


   
print(solution())



