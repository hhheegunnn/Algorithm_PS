"""https://www.acmicpc.net/problem/11286"""


"""절대값힙"""

import sys
import heapq

N = int(input())

num_list = []

#일반적인 방법 시간초과
"""
def find_min(tmp):
    min_num = sys.maxsize
    tmp_list = []

    if tmp == 0:
        if not num_list:
            return 0
    for i in range(len(num_list)):
        if min_num >= abs(num_list[i]):
            min_num = num_list[i]
            index = i
            tmp_list.append((num_list[index],index))
    
    if len(tmp_list) == 1:
        num_list.pop(tmp_list[0][1])
        return tmp_list[0][0]
    else:
        tmp_list.sort(key = lambda x: x[0])
        num_list.pop(tmp_list[0][1])
        return tmp_list[0][0]
            

result = []
for _ in range(N):

    tmp = int(input())
    
    if tmp == 0:
        #result.append(find_min(tmp))
        print(find_min(tmp))
    

    else:
        num_list.append(tmp)
"""


#우선순위 큐 사용

## input() 사용시 시간초과
result = []
for _ in range(N):

    #tmp = int(input())
    tmp = int(sys.stdin.readline())


    if tmp == 0:
        if not num_list:
            #result.append(0)
            print(0)
        else:
            #result.append(heapq.heappop(num_list)[1])
            print(heapq.heappop(num_list)[1])
    else:
        heapq.heappush(num_list, (abs(tmp),tmp))

#print(result)









