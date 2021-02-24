"""https://programmers.co.kr/learn/courses/30/lessons/42885"""

"""구명보트"""

## 문제를 잘 읽자 최대 2명 ...

def solution(people, limit):
    
    result = 0
    people.sort()
    si = 0
    ei = len(people) -1 

    while si <= ei:
        result += 1
        if people[si] + people[ei] <= limit:
            si += 1
        ei -= 1


    return result


print(solution([70,80,50],100))


