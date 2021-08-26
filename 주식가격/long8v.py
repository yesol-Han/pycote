# queue로 풀어야겠다고 생각
# 1: 2, 3, 2, 3
# 2: 3, 2, 3
# 3: 2, 3
# 2: 3
# 3: 
# 한번만 순회할 수 있도록 짜자! 는 O(n**2)...

from collections import defaultdict

def solution(prices):
    is_end = defaultdict(lambda: True)
    answer = defaultdict(int)
    for idx, price in enumerate(prices):
        if idx == len(prices) - 1: # 마지막일 때만 예외처리
            answer[(idx, price)] = 0
            is_end[(idx, price)] = False
            break
        for key, value in answer.items():
            if is_end[key] and price >= key[1]:
                answer[key] += 1
            else:
                is_end[key] = False
                
        answer[(idx, price)] += 1
    return [value for key, value in answer.items()]
