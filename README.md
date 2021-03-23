# Algorithm_PS


## Problem Solving

  - [Beakjoon Online Judge](https://www.acmicpc.net)
    - [boj implementation](https://docs.google.com/spreadsheets/d/110qOXsXB2MB15rUTlJO4cD84Q-lCNIXA6MvuVud_QDQ/edit#gid=294060215)
  - [Programmers](https://programmers.co.kr)
  - etc...



# TIPs for Python

<hr>

## zip - 짚 ✔️
```python
board = [[1,2,3],[1,2,3],[1,2,3]]

new_board = list(map(list,zip(*board)))

```

## 2차원 리스트에서 최대값 찾기
```python
array = [[1,2,3],[4,5,6],[7,8,9]]

max_ = max(map(max,array))

print(max_)
```

## deepcopy - 깊은 복사
# 수정수정수정수정수정수정수정수정
```python
array = [1,2,3]

b = array[:]
c = array

array.append(4)

print(array,b,c)
```

### 리스트에서 중복제거
```python
array = [1,2,3,1,4,3]

array = list(set(array))

print(array)
```





