def solution(prices):
    answer = [0]*len(prices)
    for t, t_price in enumerate(prices[:-1]):
        cnt = 0
        for future_price in prices[t+1:]:
            cnt+=1
            if t_price <= future_price:
                continue
            else:
                break
        answer[t] = cnt
    return answer