"""https://www.acmicpc.net/problem/19236"""


""" 청소년 상어 """

#d = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]


##########################################################
tmp = []
board = []
result = 0

for _ in range(4):
    a,b,c,d,e,f,g,h = map(int,input().split())

    tmp.append([[a,b-1],[c,d-1],[e,f-1],[g,h-1]])

    board.append([a,c,e,g])


fish = [[0,tmp[0][0][1],0,0]]
for i in range(4):
    for j in range(4):
        fish.append([tmp[i][j][0], tmp[i][j][1], i, j ])

fish.sort(key=lambda x: x[0])
result += tmp[0][0][0]
fish[tmp[0][0][0]] = [-1,-1,-1,-1]  # 처음 먹힌 물고기(0,0에 있는 물고기)를 -1,-1,-1,-1로
board[0][0] = 0 # 상어로 대체, 상어는 0


print(fish)
print(tmp)
print(board)
##########################################################



def move_fish(fish):



    d = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]

    for i in range(1,17):

        # 먹힌 물고기번호라면 다음 물고기 번호로
        if fish[i][0] == -1:
            continue 

        fish_d = fish[i][1]

        cy_cnt = 0

        # 한바퀴 다 돌았는데도 갈곳 이 없다면 그대로
        while cy_cnt < 8:
            
            #현재 물고기 좌표
            r = fish[i][2]
            c = fish[i][3]


            #다음 이동할 칸 좌표
            nr =  r + d[fish_d][0]
            nc =  c + d[fish_d][1]

            #print('next fish cord ', nr,nc)

            
            #범위 안  -> while문 종료 후 다음 물고기로 
            if 0<= nr < 4 and 0<= nc < 4:

                ## 상어면 회전
                if board[nr][nc] == 0:
                    fish_d = (fish_d+1)%8
                    cy_cnt += 1
                    continue


                # 비어 있다면
                elif board[nr][nc] == -1:
                    # fish 리스트 이동 물고기 좌표 변경
                    fish[i][2], fish[i][3] = nr, nc
                
                # 물고기가 있다면
                else:
                    fish[i][1] = fish_d

                    # 바꾸는 물고기
                    c_fish = board[nr][nc]

                    # fish 리스트에서 자리 변경할 물고기 끼리 좌표 스왑
                    fish[i][2], fish[c_fish][2] = fish[c_fish][2],fish[i][2]
                    fish[i][3], fish[c_fish][3] = fish[c_fish][3],fish[i][3]

                # 비어있던(-1) 보드에 물고기가 있던 자리는 변경 
                board[nr][nc], board[r][c] = board[r][c], board[nr][nc]

                break
                

            # 범위 오버라면 회전
            else:
                fish_d = (fish_d+1)%8
                cy_cnt += 1
                continue


def move_shark(shark_r,shark_c,shark_d):
    global result

    shark_r = fish[0][2]
    shark_c = fish[0][3]
    shark_d = fish[0][1]

    next_shark_r = shark_r + d[shark_d][0]
    next_shark_c = shark_c + d[shark_d][1]

    # 다음 상어 좌표가 범위 안이고 빈칸이 아니면 이동
    if 0<= next_shark_r < 4 and 0<= next_shark_c < 4 and board[next_shark_r][next_shark_c] != -1:

        # 상어가 먹은 물고기의 번호
        eat_fish = board[next_shark_r][next_shark_c]
        # 상어가 전에 있던 자리는 빈자리로
        board[shark_r][shark_c] = -1
        # 상어가 물고기를 먹은 자리는 상어로
        board[next_shark_r][next_shark_c] = 0
        # 상어 좌표를 최신화
        fish[0][2], fish[0][3] = next_shark_r, next_shark_c
        # 상어 방향을 최신화
        fish[0][1] = fish[eat_fish][1]
        # 먹힌 물고기 빈자리로
        fish[eat_fish] = [-1,-1,-1,-1]



    else:
        return result
"""








fish_ = move_fish(fish)









"""
