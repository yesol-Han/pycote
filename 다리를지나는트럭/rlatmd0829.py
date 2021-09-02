import collections
def solution(bridge_length, weight, truck_weights):
    truck_weights = collections.deque(truck_weights)
    ing = collections.deque()
    temp = []
    time = 0
    cnt = 0
    while True:
        time += 1
        
        if not truck_weights and not ing:
            break
        
        if truck_weights:
            i = truck_weights[0]
            if sum(ing) + i <= weight:
                ing.append(i)
                temp.append([i,bridge_length]) # 트럭kg, 거리를 같이넣어줌
                truck_weights.popleft()
        
        for j in range(cnt, len(temp)): # cnt는 거리가 -1이 된 값은 돌 필요없으므로 넘겨줄려고 추가
            temp[j][1] -= 1
            if temp[j][1] == 0: # temp에 들어있는 거리가 0이되면 대기트럭에서 뺴준다.
                cnt += 1
                temp[j][1] = -1
                ing.popleft()
    return time