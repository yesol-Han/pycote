def solution(n, computers):
    answer = 0
    n_list = [False]*n   # 컴퓨터 방문록
    
    def dfs(computer, i):
        if not n_list[i]:  # 체크하지 않은 컴퓨터이면
            n_list[i] = True
            
            for number in range(n):
                if i == number:
                    continue
                if computer[number]:    # 연결되어 있다면
                    dfs(computers[number], number)
            
            return True
        else:       # 체크했던 컴퓨터이면
            return False
    
    for num in range(n):
        if dfs(computers[num], num):
            #print(num)
            answer+=1
        
    return answer
