"""https://programmers.co.kr/learn/courses/30/lessons/43163"""


"""단어 변환"""



def diff_cnt(str_1,str_2):

    cnt = 0

    for i in range(len(str_1)):
        if str_1[i] != str_2[i]:
            cnt += 1
        
    return cnt

global answer
def dfs(begin,target,words,visited):
    answer = 0
    stack = [begin]

    while stack:
        s = stack.pop()

        if s == target:
            return answer
        
        for i in range(len(words)):
            if diff_cnt(words[i], s) == 1:
                if visited[i]:
                    continue
                visited[i] = True
                stack.append(words[i])
        answer += 1

    return answer

def dfs_recursive(begin,target,words,visited_recursive,result):

    visited_recursive.append(begin)

    if begin == target:
        #print(visited_recursive)
        result.append(len(visited_recursive))
        return

    for i in range(len(words)):
        if diff_cnt(words[i], begin) == 1:
            if words[i] not in visited_recursive:
                dfs_recursive(words[i],target,words,visited_recursive,result)
                visited_recursive.remove(words[i])


def solution(begin, target, words):
    if target not in words:
        return 0

    visited_recursive = []
    """
    visited = [False for _ in range(len(words))]
    a = dfs(begin,target,words,visited)
    return a
    """
    result = []
    dfs_recursive(begin,target,words,visited_recursive,result)
    return min(result)-1


print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))

