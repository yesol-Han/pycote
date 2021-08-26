def solution(s):
    q = [s[0]]
    for character in s[1:]:
        if q and (q[-1] == character):
            q.pop()
        else:
            q.append(character)
    if q:
        return 0
    else:
        return 1
    