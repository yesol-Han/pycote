import collections
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    distance = [0 for _ in range(n+1)]
    queue = collections.deque()
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    
    def bfs(index):
        queue.append(index)
        while queue:
            cur = queue.popleft()
            visited[cur] = True
            for next in graph[cur]:
                if visited[next] == False:
                    visited[next] = True
                    distance[next] = distance[cur] + 1
                    queue.append(next)
    bfs(1)
    maxx = max(distance)
    answer = distance.count(maxx)
    
    return answer