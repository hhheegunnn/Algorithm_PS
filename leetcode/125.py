# valid-palindrome


from collections import deque


def isPalindrome(self, s: str) -> bool:
    strs = deque()

    for c in s:
        if c.isalnum():
            strs.append(c.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


a = [1, 2, 3]
a.reverse()

print(a)
