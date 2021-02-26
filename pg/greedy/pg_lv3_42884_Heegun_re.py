"""https://programmers.co.kr/learn/courses/30/lessons/42884"""

"""단속 카메라"""


def solution(routes):
    routes.sort(key=lambda x: x[1])
    cnt = 0
    camera = -30000

    for r in routes:
        if camera < r[0]:
            cnt += 1
            camera = r[1]
    
    return cnt

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]	))




