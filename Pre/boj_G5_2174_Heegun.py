"""https://www.acmicpc.net/problem/2174"""


"""로봇 시뮬레이션"""

# git add boj_implementation/G/G5/2174/boj_G5_2174_Heegun.py
# git commit -m "[김희건] boj 로봇 시뮬레이션"


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def check_robot_crash(ny, nx):
    if 0 <= ny < B and 0 <= nx < A:
        if board[ny][nx] != [0, -1]:
            return True
        else:
            return False
    else:
        return False


def move(robot_num, robot_move, move_cnt):
    for r in range(B):
        for c in range(A):
            if board[r][c][0] == robot_num:

                d = delta[board[r][c][1]]

                if robot_move == 0:
                    for _ in range(move_cnt):
                        nr = r + d[0]
                        nc = c + d[1]
                        if not check_robot_crash(nr, nc):
                            if 0 <= nr < B and 0 <= nc < A:
                                board[nr][nc] = board[r][c]
                                board[r][c] = [0, -1]
                                r = nr
                                c = nc
                            else:
                                #print('Robot', robot_num,'crashes into the wall')
                                return [1, robot_num]
                        else:
                            #print('Robot', robot_num, 'crashes into robot', board[nr][nc][0])
                            return [2,robot_num,board[nr][nc][0]]
                    return [0]

                elif robot_move == 1:
                    # 오른쪽 회전
                    move_cnt = move_cnt % 4
                    now_d = board[r][c][1]

                    board[r][c][1] = (now_d + move_cnt) % 4

                    return [0]

                else:
                    # 왼쪽 회전
                    move_cnt = move_cnt % 4
                    now_d = board[r][c][1]

                    for _ in range(move_cnt):
                        board[r][c][1] = (now_d + 3) % 4
                        now_d = board[r][c][1]

                    return [0]



def solution():
    for comm in command:
        robot_num_ = comm[0]
        robot_move_ = comm[1]
        move_cnt_ = comm[2]
        
        tmp = move(robot_num_,robot_move_,move_cnt_)

        if tmp[0] == 1:
            return print('Robot', tmp[1],'crashes into the wall')
        elif tmp[0] == 2:
            return print('Robot', tmp[1], 'crashes into robot', tmp[2])
        else:
            continue

    return print('OK')








A, B = map(int, input().split())

# A = c # B = r

board = [[[0, -1] for _ in range(A)] for _ in range(B)]

N, M = map(int, input().split())

robot = []
command = []

for i in range(N):
    a, b, c = map(str,input().split())
    if c == 'N':
        c = '0'
    elif c == 'E':
        c = '1'
    elif c == 'S':
        c = '2'
    else:
        c = '3'
    board[B-int(b)][int(a)-1] = [i+1, int(c)]
    robot.append([B-int(b), int(a)-1, int(c)])

for _ in range(M):
    a, b, c = map(str,input().split())
    if b == 'F':
        b = '0'
    elif b == 'R':
        b = '1'
    else:
        b = '-1'
    command.append([int(a), int(b), int(c)])
#print(board)
solution()


