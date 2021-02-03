"""https://www.acmicpc.net/problem/17135"""

""" 캐슬 디펜스 """

# git add boj_implementation/G/G4/17135/boj_G4_17135_Heegun.py
# git commit -m "[김희건] boj 캐슬 디펜스"

from itertools import combinations
from copy import deepcopy


def possible_attack_list(archor):

    attack_area = []

    for ar in archor:
        # 궁수 하나 하나 하나 

        tmp = []

        for r in range(R):
            for c in range(C):
                if abs(ar[0] - r) + abs(ar[1] - c) <= D:
                    #궁수마다 공격 위치까지 (거리, r, c) 
                    tmp.append((abs(ar[0] - r) + abs(ar[1] - c),r,c))
            
        attack_area.append(tmp)

    return attack_area


def cnt_kill(enemy_set,attack_area):

    kill_cnt = 0

    while enemy_set:

        tmp = set()

        for ar in attack_area:
            # 각 궁수 ar

            kill_enemy = nearest_enemy(ar,enemy_set)

            if kill_enemy:
                tmp.add(kill_enemy)
            
            
        kill_cnt += len(tmp)

        
        enemy_set -= tmp


        emp = set()
        for y,x in enemy_set:
            if y + 1 < R:
                emp.add((y+1,x))

        enemy_set = emp

        

    return kill_cnt





def nearest_enemy(ar,enemy_list):
    ar.sort(key = lambda x: (x[0],x[2]))
    #print(ar)
    for _,r,c in ar:
        if (r,c) in enemy_list:
            return (r,c)

    return False
            


R, C , D = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(R)]

enemy_set = set()

for r in range(R):
    for c in range(C):
        if board[r][c] == 1:
            enemy_set.add((r,c))

castle = [(R,i) for i in range(C)]
archor_positions = list(combinations(castle ,3))


#print(enemy_set)
#print(archor_positions)

max_kill = 0


for archor in archor_positions:
    #print(enemy_set)

    co = deepcopy(enemy_set)

    # 궁수가 공격할 수 있는 좌표 각 궁수마다 묶어서
    attack_area = possible_attack_list(archor)
    #print(attack_area)

    killed = cnt_kill(enemy_set,attack_area)

    enemy_set = co
    if max_kill <= killed:
        max_kill = killed



print(max_kill)



    










