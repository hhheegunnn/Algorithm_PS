"""https://programmers.co.kr/learn/courses/30/lessons/72412"""

""" 순위 검색 """

# git add week_13/Re_pg_Lv2_72412_Heegun.py
# git commit -m "[김희건] pg 순위 검색"

from itertools import product
from bisect import bisect_left

def change_info(ii):
    tmp = []
    k = []
    for i in ii.split():
        if i  == 'cpp' or i == 'backend' or i == 'junior' or i == 'chicken':
            tmp.append([1,0])
        elif i == 'java' or i == 'frontend' or i == 'senior' or i == 'pizza':
            tmp.append([2,0])
        elif i == 'python':
            tmp.append([3,0])
        else:
            k.append(int(i))
            

    k.append(list(product(*tmp)))

    return k

def change_query(qq):
    tmp = []
    for q in qq.split():
        if q  == 'cpp' or q == 'backend' or q == 'junior' or q == 'chicken':
            tmp.append(1)
        elif q == 'java' or q == 'frontend' or q == 'senior' or q == 'pizza':
            tmp.append(2)
        elif q == 'python':
            tmp.append(3)
        elif q == 'and':
            continue
        elif q == '-':
            tmp.append(0)
        else:
            n = int(q)
        
    return n,tuple(tmp)

a = [1, 2, 3, 0]
b = [1, 2, 0]
c = [1, 2, 0]
d = [1, 2, 0]

condition_board = list(product(a,b,c,d))


def solution(info, query):
    answer = []

    group = [[] for _ in range(4*3*3*3)]

    for i in info:
        information = list(change_info(i))

        for j in information[1]:
            index = condition_board.index(j)
            group[index].append(information[0])

    for i in range(len(group)):
        if group[i]:
            group[i] = sorted(group[i])
    
    for q in query:
        n,qu = change_query(q)
        
        gi = condition_board.index(qu)


        a = len(group[gi]) - bisect_left(group[gi],n)
        answer.append(a)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["- and - and - and - 150"]))




