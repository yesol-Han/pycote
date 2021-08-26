import collections
def solution(places):
    n = len(places)
    answer = []
    dx, dy = [-1,1,0,0], [0,0,-1,1] # 상하좌우
    d_x, d_y = [-1,-1,1,1], [-1,1,-1,1] # 대각선
    
    for i in places:
        graph = []
        for j in i:
            graph.append(list(j))
            
        queue = collections.deque()
        
        for x in range(len(graph)):
            for y in range(len(graph)):
                if graph[x][y] == 'P':
                    queue.append((x,y))
                    
        def bfs():
            while queue:
                x,y = queue.popleft()
                for k in range(4): # 상하좌우 확인
                    temp_x, temp_y = x,y
                    for _ in range(2): # 상하좌우는 2거리 까지 확인해야함
                        nx = temp_x + dx[k]
                        ny = temp_y + dy[k]
                        if 0 <= nx < n and  0 <= ny < n:
                            if graph[nx][ny] == 'X': # X에 막혀있으면 더이상 갈 필요없어서 break
                                break
                            elif graph[nx][ny] == 'P': # P를 만나면 거리두기를 안지켰으므로 False
                                return False
                            temp_x, temp_y = nx, ny
                        else:
                            break
                            
                for k in range(4): # 대각선 확인
                    n_x = x + d_x[k]
                    n_y = y + d_y[k]
                    if 0 <= n_x < n and  0 <= n_y < n:
                        if graph[n_x][n_y] == 'P': # 대각선이 P일 경우 x,y와 n_x, n_y 근처 두곳이 모두 X여야만 한다.
                            if graph[n_x - d_x[k]][n_y] == 'X' and graph[n_x][n_y  - d_y[k]] == 'X':
                                continue
                            else: # 두곳중 한곳이라도 X가 아니면 False
                                return False
            return True
        check = bfs()
        if check:
            answer.append(1)
        else:
            answer.append(0)
    return answer