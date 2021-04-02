"""https://www.acmicpc.net/problem/20055"""


"""컨베이어벨트위의로봇"""

from collections import deque

N,K = map(int,input().split())

#belt = deque(list(map(int,input().split())))

tmp = list(map(int,input().split()))
belt = deque([])
for t in tmp:
    belt.append([t,0])


#print(belt)


def rotate(belt):

    if belt[N-1][1] == 1:
        belt[N-1][1] = 0

    belt.rotate(1)

    if belt[N-1][1] == 1:
        belt[N-1][1] = 0

def step_2(belt):

    for i in range(N-2,-1,-1):
        if belt[i][1] == 1:
            if belt[i+1][1] == 0 and belt[i+1][0] >= 1:
                belt[i+1][1] = 1
                belt[i+1][0] -= 1
                belt[i][1] = 0


def up_robot(belt):

    if belt[0][1] == 0 and belt[0][0] >= 1:
        belt[0][1] = 1
        belt[0][0] -= 1


def check_end(belt):
    cnt = 0

    for d,_ in belt:
        if d <= 0 :
            cnt += 1

    
    if K <= cnt:
        return True
    else:
        return False



def solution():
    C = 1

    while True:
        rotate(belt)
        step_2(belt)
        up_robot(belt)

        if check_end(belt):
            return C
        else:
            C += 1

print(solution())
        
