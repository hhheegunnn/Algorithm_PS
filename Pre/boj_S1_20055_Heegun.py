"""https://www.acmicpc.net/problem/20055"""


"""컨베이어 벨트 위의 로봇"""


from collections import deque

N,K = map(int,input().split())

# N 컨베이어 벨트 K 내구도 0 한계치



belt = deque([[0,x] for x in map(int,input().split())])
cnt = 0


while True:

    cnt += 1

    #벨트 회전 #떨어지는 위치면 떨어진다
    if belt[N-1][0] == 1:
        belt[N-1][0] = 0
        belt.appendleft(belt.pop())
        #belt.rotate(1)
    else:
        belt.appendleft(belt.pop())
        #belt.rotate(1)



    # 로봇이동,내구도 1감소 # 떨어지는 위치면 떨어지지
    for i in range(N-1,-1,-1):
        if belt[i][0] == 1:
            if i == N-1:
                belt[i][0] = 0
                continue
            else:
                if belt[i+1][0] == 0 and belt[i+1][1] >= 1:
                    belt[i+1][0] = 1
                    belt[i+1][1] -= 1
                    if belt[i+1][1] == 0:
                        K -= 1
                    belt[i][0] = 0
                else:
                    continue


        else:
            continue

    

    #시작위치에 로봇이 없으면 로봇 하나 올리고 내구도 1감소
    if belt[0][0] == 0 and belt[0][1] >= 1:
        belt[0][0] = 1
        belt[0][1] -= 1
        if belt[0][1] == 0:
            K-= 1




    #내구도가 0인 칸의 개수가 K개 이상이면 종료

    if K <= 0:
        print(cnt)
        break






    
    








