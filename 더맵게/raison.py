import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    count = 0
    while True:
        count = count + 1
        a, b = heapq.heappop(scoville) , heapq.heappop(scoville)

        heapq.heappush(scoville, a + (b*2))
        c = heapq.heappop(scoville)


        if c >= K:

            answer = count

            return answer
        elif len(scoville) == 1 and c < K:
            answer = -1
            return answer
        heapq.heappush(scoville, c)
