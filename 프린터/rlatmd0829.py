def solution(priorities, location):
    result = []
    temp = []
    for idx, i in enumerate(priorities):
        temp.append([i,idx]) # temp에 index값과 priorities값 같이 저장
    
    while True:
        if len(result) == len(priorities): # while문 종료 조건
            break
            
        if priorities[0] != max(priorities): # priorities에 가장 큰 값과 맨앞 값이 다르면 맨 뒤로 보냄
            priorities.append(priorities.pop(0))
            temp.append(temp.pop(0))
            
        else: # 맨앞 값이 가장 큰 값이면
            result.append(temp[0]) # result에 temp값을 담는다. ex) [[9, 2], [1, 3], [1, 4], [1, 5], [1, 0], [1, 1]]
            priorities[0] = 0 # max값을 새로 구해야 하기떄문에 0으로 초기화
    
    for idx,i in enumerate(result): # result안에는 출력 순서대로 들어와있다. 
        if i[1] == location: # location과 같은 인덱스 출력
            return idx+1