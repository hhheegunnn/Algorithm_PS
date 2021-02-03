"""https://www.acmicpc.net/problem/2564"""


"""경비원"""

# git add boj_implementation/S/S1/2564/boj_S1_2564_Heegun.py
# git commit -m "[김희건] boj 경비원"



def solution(c,r,market_list,d):
    ssum  = 0
    
    for i in market_list:
        if d[0] == i[0]:
            ssum += abs(d[1]-i[1])
        elif d[0] == 1:
            if i[0] == 3:
                ssum += (d[1] + i[1])
            elif i[0] == 4:
                ssum += (c-d[1] + i[1])
            else:
                ssum += r
                ssum += min(d[1]+i[1], c - d[1] + c - i[1])
        elif d[0] == 2:
            if i[0] == 3:
                ssum += (d[1] + r-i[1])
            elif i[0] == 4:
                ssum += (c- d[1] + r - i[1])
            else:
                ssum += r
                ssum += min(d[1]+i[1], c - d[1] + c - i[1])
        elif d[0] == 3:
            if i[0] == 1:
                ssum += (d[1] + i[1])
            elif i[0] == 2:
                ssum += (r- d[1] + i[1])
            else:
                ssum += c
                ssum += min(d[1]+i[1], r - d[1] + r - i[1])
        elif d[0] == 4:
            if i[0] == 1:
                ssum += (d[1] + c - i[1])
            elif i[0] == 2:
                ssum += (r - d[1] + c - i[1])
            else:
                ssum += c
                ssum += min(d[1]+i[1], r - d[1] + r - i[1])


    return ssum






C , R = map(int,input().split())
Market_list = []
for _ in range(int(input())):
    Market_list.append(list(map(int,input().split())))
D = list(map(int,input().split()))

print(solution(C,R,Market_list,D))



