from collections import defaultdict, deque
que = deque()
def solution(n, edge):
    map = defaultdict(list) # 지도
    for n in edge:
        map[n[0]].append(n[1])
        map[n[1]].append(n[0])
    graph = {} # 최단 distance를 담을 딕셔너리
    graph[1] = 0
    que = deque([1])
    while len(que):
        if len(graph) == n:
            break
        node = que.popleft()
        next_nodes = map[node][:]
        for next_node in next_nodes:
            if next_node not in graph: 
                que.append((next_node))
                map[next_node].remove(node)
                map[node].remove(next_node)
            
                graph[next_node] = graph[node] + 1
    return len([1 for key, value in graph.items() if value == max(graph.values())])