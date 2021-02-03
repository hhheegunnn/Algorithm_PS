"""https://www.acmicpc.net/problem/1783"""


"""병든 나이트"""


N , M = map(int,input().split())



# 나이트는 항상 오른쪽으로 1칸 또는 2칸만 이동
# 나이트가 갈 수 있는 최대 칸수 -> 한칸씩만 이동하는게 최대



# 나이트 움직임이 4번 이상일 경우 가로 M은 최소 7 이상 세로 N은 최소 3이상 
if M >= 7 and N >=3:
    cnt = 5
    M -= 7  #4번 이동 후 남은 가로 칸 수 
    cnt += M
        


# 세로가 2일 경우 가로로 1칸씩 이동 불가능 -> 2칸씩 이동
# 세로가 1일 경우 못움직임
# 세로가 3 이상이고 가로가 7보다 작을 경우 -> 1칸씩 이동 
else:
    cnt = 1

    if N >= 3:
        cnt += (M-1)
        if cnt >= 4:   # 움직임이 4번 이상인 경우 이동 가능 칸을 4로
            cnt = 4
    elif N == 1:
        cnt = 1
    else:
        cnt += ((M-1)//2)
        if cnt >= 4:
            cnt = 4


print(cnt)


"""
n,m = map(int,input().split())
cnt = 0

if n == 1:
    cnt = 1 

elif n == 2:
    cnt = min(4,int((m+1)/2))

elif m < 7:
    cnt = min(m,4)
    
else:
    cnt = 5 + m - 7

print(cnt)
"""




