"""https://programmers.co.kr/learn/courses/30/lessons/72410"""


""" 신규 아이디 추천 """

# git add week_13/pg_Lv1_72410_Heegun.py
# git commit -m "[김희건] pg 신규 아이디 추천"



def solution(new_id):

    # 1
    new_id = new_id.lower()

    # 2

    result = ''

    for i in range(len(new_id)):
        if new_id[i].isalpha():
            result += new_id[i]
        elif '0'<= new_id[i] <= '9':
            result += new_id[i]
        elif new_id[i] == '-' or new_id[i] == '_' or new_id[i] =='.':
            result += new_id[i]
        else:
            continue

    # 3
    while True:
        if ".." in result:
            result = result.replace("..",".")
        else:
            break


    # 4
    if result:
        if result[0] == '.':
            result = result.lstrip('.')
    if result:
        if result[-1] == '.':
            result = result.rstrip('.')

    # 5

    if not result:
        result = 'a'
 
    # 6

    if len(result) >= 16:
        result = result[:15]

    if result[-1] == '.':
        result = result.rstrip('.')

    # 7 

    if len(result) <= 2:
        while len(result) != 3:
            result += result[-1]
        
    


    return result

print(solution("..ad....d"))


