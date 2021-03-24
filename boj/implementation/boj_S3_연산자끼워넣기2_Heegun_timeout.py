"""https://www.acmicpc.net/problem/15658"""



"""연산자 끼워넣기"""

from itertools import permutations

import sys



N = int(input())

numbers = list(map(int,input().split()))

op_num = list(map(int,input().split()))

op = []

for i in range(4):
    if i == 0:
        op = op+[1 for _ in range(op_num[i])]
    elif i == 1:
        op = op+[2 for _ in range(op_num[i])]
    elif i == 2:
        op = op+[3 for _ in range(op_num[i])]
    elif i == 3:
        op = op+[4 for _ in range(op_num[i])]

possible_op_list = list(set(permutations(op,N-1)))


def cal(N,numbers,op_list):

    result = numbers[0]
    
    for i in range(1,len(numbers)):
        if op_list[i-1] == 1:
            result += numbers[i]
        elif op_list[i-1] == 2:
            result -= numbers[i]
        elif op_list[i-1] == 3:
            result *= numbers[i]
        else:
            if result < 0:
                result = (result*-1)//numbers[i]
                result *= -1
            else:
                result //= numbers[i]

    return result

max_ = -sys.maxsize
min_ = sys.maxsize

for opers in possible_op_list:

    tmp = cal(N,numbers,opers)

    max_ = max(max_,tmp)
    min_ = min(min_,tmp)

print(max_)
print(min_)




        
