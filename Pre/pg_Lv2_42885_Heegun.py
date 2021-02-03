"""https://programmers.co.kr/learn/courses/30/lessons/42885"""

"""구명보트"""

##문제를 잘 읽자 최대최대최대2명2명2명

from collections import deque

def solution(people,limit):

    cnt = 0

    people.sort()

    s = 0
    e = len(people) - 1

    while s <= e:
        cnt += 1
        if people[s] + people[e] <= limit:
            s += 1
        e -= 1            
    
    return cnt


#### deque 사용시 통과는 하는데 효율성 측면에서 index 접근이 빠르다고 나옴
"""

def solution(people,limit):

    cnt = 0
    
    people.sort()

    people = deque(people)

    while people:
        if len(people) == 1:
            cnt += 1
            break

        if people[-1] + people[0] > limit:
            people.pop()
            cnt += 1
        else:
            people.pop()
            people.popleft()
            cnt += 1

    return cnt
"""

print(solution([10, 10, 80]	,100))
#print(solution([70, 80, 50],100))
#print(solution([70],100))