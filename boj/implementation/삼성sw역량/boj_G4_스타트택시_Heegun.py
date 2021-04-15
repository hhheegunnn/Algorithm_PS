"""https://www.acmicpc.net/problem/19238"""


"""스타트택시"""

from collections import deque
import heapq


N , M , fuel = map(int,input().split())


board = [ list(map(int,input().split())) for _ in range(N) ]

tr, tc = map(int,input().split())

start_taxi = [tr-1,tc-1]

end_list = [0]

for i in range(1,M+1):
    a,b,c,d = map(int,input().split())

    board[a-1][b-1] = -i
    end_list.append((c-1,d-1))


def bfs_find_guest(sr,sc):

    # 도착지에 승객
    if board[sr][sc] < 0 :
        return (0, sr, sc, -board[sr][sc])


    visited = [[-1 for _ in range(N)] for _ in range(N)]

    q = deque([(sr,sc)])

    visited[sr][sc] = 0

    meet_guest = []

    while q:

        r,c = q.popleft()

        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:

            nr, nc = r + dr, c + dc

            if 0<= nr < N and 0<= nc < N and visited[nr][nc] == -1:

                if board[nr][nc] != 1 and board[nr][nc] == 0:

                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr,nc))

                elif board[nr][nc] != 1 and board[nr][nc] < 0:

                    visited[nr][nc] = visited[r][c] + 1
                    if not meet_guest:
                        #meet_guest.append((visited[nr][nc], nr, nc))
                        heapq.heappush(meet_guest, (visited[nr][nc], nr, nc, -board[nr][nc]))
                    else:
                        if meet_guest[0][0] < visited[nr][nc]:
                            #meet_guest.sort(key = lambda x : (x[0],x[1],x[2]))

                            return heapq.heappop(meet_guest)
                        else:
                            #meet_guest.append((visited[nr][nc], nr, nc))
                            heapq.heappush(meet_guest, (visited[nr][nc], nr, nc, -board[nr][nc]))

                else:
                    continue
                 
    if meet_guest:
        return heapq.heappop(meet_guest)
    else:
        return False


def bfs_go_end(sr,sc,guest_index):

    board[sr][sc] = 0

    visited = [ [-1 for _ in range(N)] for _ in range(N)]

    q = deque([(sr,sc)])

    visited[sr][sc] = 0

    while q:

        r,c = q.popleft()

        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:

            nr,nc = r+ dr, c + dc

            if 0<= nr < N and 0<= nc < N and visited[nr][nc] == -1:

                if board[nr][nc] != 1:

                    if (nr,nc) == end_list[guest_index]:

                        visited[nr][nc] = visited[r][c] + 1
                        return (visited[nr][nc],nr,nc)
                    
                    else:
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr,nc))

    return (-1,-1,-1)



def solution():
    global fuel
    global start_taxi

    for _ in range(M):


        nearest_guest = bfs_find_guest(start_taxi[0],start_taxi[1])

        if nearest_guest == False:
            return -1

        if fuel - nearest_guest[0] <= 0:
            return -1
        else:
            fuel -= nearest_guest[0]

        use_fuel,start_taxi[0],start_taxi[1] = bfs_go_end(nearest_guest[1],nearest_guest[2],nearest_guest[3])

        if (use_fuel,start_taxi[0],start_taxi[1]) == (-1,-1,-1):
            return -1

        if fuel - use_fuel < 0 :
            return -1
        else:
            fuel -= use_fuel
            fuel += (use_fuel*2)

        
    return fuel


print(solution())


    
"""
3 2 15
0 1 0
0 0 0
0 0 0
1 1
2 2 3 3
3 3 2 1

""" 