"""https://www.acmicpc.net/problem/19238"""


""" 스타트 택시 """

def find_shortest_path():
    pass




N,M,O = map(int,input().split())


board = [list(map(int,input().split())) for _ in range(N)]

sr,sc = map(int,input().split())

sr -= 1
sc -= 1

guest = [list(map(int-1,input().split())) for _ in range(M)]

print(guest)







