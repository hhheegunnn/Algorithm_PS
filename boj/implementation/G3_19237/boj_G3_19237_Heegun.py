"""https://www.acmicpc.net/problem/17471"""


"""어른 상어"""


direction = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]

N, M, K = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]


# 상어 초기 방향
shark_d = list(map(int,input().split()))
shark_d.insert(0,0)



# 상어 우선순위
shark_p = [[0] for _ in range(M+1)]
for i in range(1,M+1):
    for _ in range(4):
        tmp = list(map(int,input().split()))
        shark_p[i].append(tmp)

# 초기 상태
shark_cord = [[] for _ in range(M+1)]
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            s_num = board[i][j]
            board[i][j] = [s_num, K]
            shark_cord[s_num]=[i,j]



def each_shark_target(n,d,r,c):
    
    prio = shark_p[n][d]

    # 인접에 비어있는 칸이 있을 경우
    for i in prio:
        dr = direction[i][0]
        dc = direction[i][1]

        nr = r + dr
        nc = c + dc

        if 0<= nr < N and 0<= nc < N:
            # 비어있고 충돌 안일어나면
            # 상어를 오름차순으로 돌리므로 다음 번호 상어에서 충돌이 나면 그 상어는 끝
            if board[nr][nc] == 0:
                #board[nr][nc] = [n,s]
                #target_cord[n] = [nr,nc]
                shark_d[n] = i
                #board[r][c] = [n,s]
                return [nr,nc]

    # 인접에 비어있는 칸이 없을 경우
    for i in prio:
        dr = direction[i][0]
        dc = direction[i][1]

        nr = r + dr
        nc = c + dc

        if 0<= nr < N and 0<= nc < N:
            if board[nr][nc][0] == n:
                shark_d[n] = i
                return [nr,nc]

    return [r,c]


def shark_move():

    for i in range(1,M+1):
        r,c = shark_cord[i][0], shark_cord[i][1]
        if r != -1 and c != -1:
            board[r][c] = [i,K]
    

def remove_smell():

    for i in range(N):
        for j in range(N):
            # 빈곳이 아니고
            if board[i][j] != 0:
                # 상어가 없는 곳이면
                if [i,j] not in shark_cord:
                    # 냄새 감소
                    board[i][j][1] -= 1
                    # 냄새 감소했는데 0 이면 빈 칸으로
                    if board[i][j][1] == 0:
                        board[i][j] = 0

cnt = 0

while True:

    cnt += 1

    if cnt > 1000:
        print(-1)
        break

    target_cord = [[] for _ in range(M+1)]
    for i in range(1,M+1):
        sr = shark_cord[i][0]
        sc = shark_cord[i][1]
        sd = shark_d[i]
        if sd != -1:
            target_cord[i] = each_shark_target(i,sd,sr,sc)
        else:
            target_cord[i] = [-1,-1]

    for i in range(M,0,-1):
        if target_cord[i] in target_cord[1:i]:
            shark_cord[i] = [-1,-1]
            shark_d[i] = -1
        else:
            shark_cord[i] = target_cord[i]

    shark_move()

    remove_smell()

    if sum(shark_d[2:M+1]) == -1*(M-1):
        print(cnt)
        break



"""
print(shark_cord)

print(shark_d)
print(board)

    

def first_move():
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                s_num = board[i][j][0]
                s_d = board[i][j][1]
                rs = board[i][j][2]


[[], [[2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 2, 1], [4, 3, 1, 2]], [[2, 4, 3, 1], [2, 1, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3]], [[4, 3, 2, 1], [1, 4, 3, 2], [1, 3, 2, 4], [3, 2, 1, 4]], [[3, 4, 1, 2], [3, 2, 4, 1], [1, 4, 2, 3], [1, 4, 2, 3]]]
                
"""
