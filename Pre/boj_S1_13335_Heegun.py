"""https://www.acmicpc.net/problem/13335"""



""" 트럭 """


# git add boj_implementation/S/S1/13335/boj_S1_13335_Heegun.py
# git commit -m "[김희건] boj 트럭"

from collections import deque

n, w, l = map(int,input().split())


tw_list = list(map(int,input().split()))
for _ in range(w):
    tw_list.append(0)

bridge = deque([0 for _ in range(w)])

cnt = 1


bridge.popleft()
bridge.append(tw_list[0])


def check_sum(bridge,next_t,l):
    if sum(bridge) + next_t > l:
        return False
    else:
        return True

i = 1

while True:

    if i >= w+n:
        break

    next_truck = tw_list[i]

    bridge.popleft()

    if check_sum(bridge,next_truck,l):
        bridge.append(next_truck)
        cnt += 1
        i += 1

    else:
        bridge.append(0)
        if sum(bridge)!= 0:
            cnt += 1
    #print(bridge,cnt)


if n == 1:
    print(w+1)
else:
    print(cnt)














            


    







    






    





    

