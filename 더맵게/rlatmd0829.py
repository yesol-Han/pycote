import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 1:
        x = heapq.heappop(scoville)
        if x >= K:
            break
        if len(scoville) == 0:
            if x < K:
                return -1
        else:
            y = heapq.heappop(scoville)
            heapq.heappush(scoville, x+y*2)
            answer += 1
        
    return answer