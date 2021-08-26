from collections import deque
def solution(_list, _loc):
    max_prior = max(_list)
    d_list = deque([(v, i) for i, v in enumerate(_list)])

    cnt = 1
    while True:
        now = d_list.popleft()
        if d_list and (now[0] < max(d_list)[0]):
            d_list.append(now)
        else:
            if now[1] == _loc:
                return cnt
            else:
                cnt += 1

    return cnt