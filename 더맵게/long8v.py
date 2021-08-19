import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    try: 
        lowest = heapq.heappop(scoville)
        while lowest < K:
            second_lowest = heapq.heappop(scoville)
            heapq.heappush(scoville, lowest + second_lowest *2)
            lowest = heapq.heappop(scoville)
            answer += 1
    except IndexError:
        return -1
    return answer