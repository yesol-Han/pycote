from collections import deque
def solution(s):
    stack = []
    s = sorted([i for i in s[2:-2].split("},{")], key = len)

    for _s in s:
        _s = list(map(int, _s.split(",")))
        for each_item in _s:
            if (each_item not in stack[:len(_s)]):
                stack.append(int(each_item))
        
    return stack