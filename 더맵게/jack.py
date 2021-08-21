# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3#

# 1차 풀이 (정확성 통과, 효율성 전부 실패) -> 소트에서 문제가 생기는 것으로 판단됨..
def solution(scoville, K):
    def _make_two_to_one(a, b):
        return a+(b*2)
    
    if min(scoville) > K:
        return 0
    
    _shuffle = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        new = _make_two_to_one(scoville[0], scoville[1])
        scoville = [new] + scoville[2:]
        scoville.sort()
        _shuffle += 1
        
    return _shuffle

# heapq
# 아예 생각도 못해봤던 자료구조.. 입출력 타임에 소팅을 해주는게 엄청난 장점이고, 리스트 인터페이스를 그대로 가져가는게 신기..
# https://docs.python.org/ko/3/library/heapq.html
import heapq
def solution(scoville, K):
    heap = []
    [heapq.heappush(heap, i) for i in scoville]

    def _make_two_to_one(a, b):
        return a+(b*2)

    _shuffle = 0
    while heap[0] < K:
        if len(heap) == 1:
            return -1
        elif len(scoville) == 2:
            if _make_two_to_one(heap[0], heap[1]) > K:
                return _shuffle + 1
            else: 
                return -1
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        new = _make_two_to_one(a, b)
        heapq.heappush(heap, new)
        _shuffle += 1
    return _shuffle
