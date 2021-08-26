def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]: # 현재 값보다 다음 값이 크거나 같다면 count += 1
                count += 1
            else: # 현재 값보다 다음값이 작다면 더이상 그 다음값은 볼 필요 없다.
                count += 1  # 문제에서 다음 값에서 바로 가격이 떨어졌더라도 1초는 떨어지지 않은것으로 본다.
                break 
        answer.append(count)
    return answer