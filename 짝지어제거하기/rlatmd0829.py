def solution(s):
    result = []
    for i in s:
        if result: # result가 있을때
            if result[-1] == i: # result에 맨 마지막값과 현재 넣는 값이 같다면 현재 들어있는 값을 빼준다.
                result.pop()
            else: # 같지 않다면 그대로 넣어준다.
                result.append(i)
        else: # result에 처음 넣을때는 비교 값이 없으므로 그냥 넣어준다.
            result.append(i)
    
    if result: # result에 값이 있다면 모두 못지운 경우이다.
        return 0
    else:
        return 1