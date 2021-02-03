"""https://programmers.co.kr/learn/courses/30/lessons/42860"""

"""조이스틱"""


def solution(name):
    mv_cnt = 0
    diff_list = []

    for c in name:
        k = min(ord(c)-65, 91-ord(c))
        diff_list.append(k)

    index = 0

    while True:
        mv_cnt += diff_list[index]
        diff_list[index] = 0
        if sum(diff_list) == 0 :
            break
        l, r = 1,1
        while diff_list[index-l] == 0:
            l += 1
        while diff_list[index+r] == 0:
            r += 1
        if l < r :
            mv_cnt += l
            index += -l
        else:
            mv_cnt += r
            index += r
        
  

    return mv_cnt

print(solution('BBABAAAB')) #9 -> =
print(solution('ABABAAAAABA'))
