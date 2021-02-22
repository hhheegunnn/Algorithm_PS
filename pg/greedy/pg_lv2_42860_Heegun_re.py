"""https://programmers.co.kr/learn/courses/30/lessons/42860"""



"""조이스틱"""


def solution(name):

    diff_list = []
    mv_cnt = 0

    for c in name:
        k = min(ord(c)-65, 91-ord(c))
        diff_list.append(k)
    
    index = 0 
    turn_flag = True
    
    while True:
        mv_cnt += diff_list[index]
        diff_list[index] = 0
        if sum(diff_list) == 0 :
            break

        if turn_flag:
            l,r = 1,1

            while diff_list[index-l] == 0:
                l += 1
            while diff_list[index+r] == 0:
                r += 1

            if l < r :
                mv_cnt += l
                index += -l
                turn_flag = False
            else:
                mv_cnt += r
                index += r
        
        else:
            mv_cnt += 1
            index += -1

        



    return mv_cnt



print(solution("ABM"))
print(solution('AABAAAB'))
print(solution('BBABAAAB'))
print(solution('AABAAAB'))