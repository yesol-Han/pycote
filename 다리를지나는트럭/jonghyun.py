from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights) 
    
    while True:
        answer += 1
        bridge.popleft()
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
            else:
                bridge.append(0)
        else:
            if sum(bridge) > 0:
                bridge.append(0)
            else:
                return answer