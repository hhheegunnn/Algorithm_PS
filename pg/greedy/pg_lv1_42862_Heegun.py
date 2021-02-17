"""https://programmers.co.kr/learn/courses/30/lessons/42862"""


""" 체육복 """



def solution(n, lost, reserve = list):
    
    reserve_ = set(reserve)-set(lost)
    lost_ = set(lost)- set(reserve)

    for i in reserve_:
        f = i - 1
        b = i + 1
        if f in lost_:
            lost_.remove(f)
        elif b in lost_:
            lost_.remove(b)
        
    return n - len(lost_)

print(solution(5,[2,4],[1,3,5]))