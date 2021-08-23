
# 스택으로 이 문제 어떻게 구현해야 할지 모르겠어서
# 이중 포문으로 풀었습니다..

def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        count = 0
        cnt = prices[i]

        for j in range(i+1, len(prices)):
            count += 1
            if cnt <= prices[j]:
                pass
            else:
                answer[i] = count
                break
        answer[i] = count

    return answer


prices = [1, 2, 3, 2, 3]

solution(prices)