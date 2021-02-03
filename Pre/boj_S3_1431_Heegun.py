"""https://www.acmicpc.net/problem/1431"""


"""시리얼 번호"""


# git add week_06/boj_S3_1431_Heegun.py
# git commit -m "[김희건] boj 시리얼 번호 [파이썬 리스트 정렬 다중조건]"


N = int(input())

g_list = []



for _ in range(N):
    tmp = input()
    num = 0
    for i in tmp:
        if 48 <= ord(i) <= 57:
            num += (ord(i)-48)
        else:
            continue
    
    g_list.append((len(tmp),num,tmp))

g_list.sort(key=lambda x: (x[0],x[1],x[2]))

for i in g_list:
    print(i[2])


    
    
