from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    
    bridge = deque([0] * bridge_length)
    _time = 0
    on_bridge_weight = 0
    while truck_weights or (sum(bridge) != 0):
        b_now = bridge.popleft()
        on_bridge_weight -= b_now
        # if (bridge has empty_place) and (bridge_weight + now_truck_weight) < weight:
        
        if truck_weights and (on_bridge_weight + truck_weights[0] <= weight):
            t_now = truck_weights.popleft()
            bridge.append(t_now)
            on_bridge_weight += t_now
            
        else:
            bridge.append(0)
        _time += 1  
    return _time