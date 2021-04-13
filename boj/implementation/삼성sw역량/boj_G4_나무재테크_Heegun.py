""" https://www.acmicpc.net/problem/16235 """



""" 나무 재테크 """

# N N
# r,c 1부터 - > 수정
# 봄
# 나무 M개 한칸에 여러개 가능 - > x차원 -> 여러개 어린 나무부터 양분 먹 , 나이만큼 양분 못먹으면 즉사
# 
# 여름 죽은 나무 양분 -> 나이//2
# 가을 나무 번식 나이 5의 배수 나무 인접 8칸 나이 1인 나무 생성
# 겨울 땅에 양분 추가 입력으로

##### board_tree 각 요소를 리스트가 아닌 defaultdict로 

from collections import defaultdict

N,M,K = map(int,input().split())

add_board = [list(map(int,input().split())) for _ in range(N)]
#board_tree = [[[] for _ in range(N)] for _ in range(N)]
board_tree = [[defaultdict(lambda : 0) for _ in range(N)] for _ in range(N)]
board_energy = [[5 for _ in range(N)] for _ in range(N)] 

for _ in range(M):
    x, y , z = map(int,input().split())

    #board_tree[x-1][y-1].append(z)
    board_tree[x-1][y-1][z] += 1



def spring_summer():
    for r in range(N):
        for c in range(N):

            board_tree[r][c].sort()

            for tree_index in range(len(board_tree[r][c])):
                
                if board_energy[r][c] - board_tree[r][c][tree_index] >= 0:
                    board_energy[r][c] -= board_tree[r][c][tree_index]
                    board_tree[r][c][tree_index] += 1
                
                else:
                    
                    for index in range(tree_index,len(board_tree[r][c])):
                        board_energy[r][c] += board_tree[r][c][index]//2

                    board_tree[r][c] = board_tree[r][c][:tree_index]
                    break

def spring_summer_defaultdict():
    for r in range(N):
        for c in range(N):

            dt = 0
            tmp = defaultdict(lambda:0)

            for age,tn in sorted(board_tree[r][c].items()):
                alive = min(board_energy[r][c]//age, tn)
                dead = tn - alive
                if alive > 0:
                    board_energy[r][c] -= age*alive
                    tmp[age+1] += alive
                dt += (age//2)*dead
            
            board_tree[r][c] = tmp
            board_energy[r][c] += dt

def fall():

    for r in range(N):
        for c in range(N):

            for age, tree_n in board_tree[r][c].items():
                if age%5 == 0 and tree_n != 0:

                    for dr,dc in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:

                        nr,nc = r + dr, c + dc

                        if 0<= nr < N and 0<= nc < N:
                            #board_tree[nr][nc].append(1)
                            board_tree[nr][nc][1] += tree_n

def winter():
    for r in range(N):
        for c in range(N):
            board_energy[r][c] += add_board[r][c]

def solution():


    for _ in range(K):
        #spring_summer()
        spring_summer_defaultdict()
        fall()
        winter()


    #####################
    result = 0
    for i in range(N):
        for j in range(N):
            if board_tree[i][j]:
                result += len(board_tree[i][j])

    result_ver2 = 0
    for i in range(N):
        for j in range(N):
            for _,tn in board_tree[i][j].items():
                result_ver2 += tn

    #return result
    return result_ver2


print(solution())

"""
5 1 1
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 4
"""



