"""https://www.acmicpc.net/problem/15686"""


"""치킨 배달"""


# git add boj_implementation/G/G5/15686/boj_G5_15686_Heegun.py
# git commit -m "[김희건] boj 치킨 배달"

from itertools import combinations

def chicken_coordinate(board,m):
    c_coordinate = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 2:
                c_coordinate.append((r,c))
    
    c_c = list(combinations(c_coordinate,m))

    return c_c



def solution(n,board,chicken):

    min_sum = 0

    for r in range(n):
        for c in range(n):

            if board[r][c] == 1:
                min_d = []
                
                for i in chicken:
                    min_d.append(abs(r-i[0]) + abs(c-i[1]))
                min_sum += min(min_d)
        
    
    return min_sum


    
    



N , M = map(int,input().split())

Board = [list(map(int,input().split())) for _ in range(N)]

Chicken = chicken_coordinate(Board,M)

result = []

for chic in Chicken:

    result.append(solution(N,Board,chic))

print(min(result))