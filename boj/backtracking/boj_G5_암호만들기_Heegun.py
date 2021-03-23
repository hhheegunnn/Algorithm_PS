"""https://www.acmicpc.net/problem/1759"""



"""암호만들기"""



L,C = map(int,input().split())

alphs = list(map(str,input().split()))

visited = [False for _ in range(C)]

alphs.sort()

result = []

def check_possible(arr):

    m = ['a','e','i','o','u']
    m_cnt = 0
    j_cnt = 0

    for i in arr:
        if i in m:
            m_cnt += 1
        else:
            j_cnt += 1

    if m_cnt >= 1 and j_cnt >= 2:
        return True
    else:
        return False




def dfs(r,idx):

    if len(r) == L:
        if check_possible(result):
            print(''.join(result))
            return
        else:
            return

    
    for i in range(idx,C):

        if not visited[i]:

            visited[i] = True
            result.append(alphs[i])

            dfs(result,i+1)

            visited[i] = False
            result.pop()


dfs(result,0)

