"""https://www.acmicpc.net/problem/5430"""


""" AC """



# git add boj_implementation/S/S2/5430/Re_boj_S2_5430_Heegun.py
# git commit -m "[김희건] boj AC rstip과 시간초과 생각하자"
from collections import deque
import sys
#input = sys.stdin.readline



# deque 사용시 192 ms
# list 사용시 3824 ms 

# 유의미한 차이


def AC(p,num_list):
    reverse_flag = False

    if len(num_list) < p.count('D'):
        return print('error')

    for c in p:
        if c == 'R':
            reverse_flag = not reverse_flag
        elif c == 'D':
            index = 0
            if reverse_flag:
                index = -1
            else:
                index = 0
            
            if num_list:
                if index == -1:
                    num_list.pop()
                else:
                    num_list.popleft()
            else:
                return print('error')

    if num_list:
        if reverse_flag:
            return print('[' + ','.join(reversed(num_list)) + ']')
        else:
            return print('[' + ','.join(num_list) + ']')
    
    return print('[]')

            

    

T = int(input())

#####
#####

for _ in range(T):

    # 수행할 함수
    p = input()

    # 배열에 들어있는 수의 개수
    n = int(input())

    # 개같이 입력받는 배열 -> rstrip()
    num_list = deque(input().rstrip()[1:-1].split(','))

    if n == 0:
        num_list = []
    

    AC(p,num_list)
    



    




    








