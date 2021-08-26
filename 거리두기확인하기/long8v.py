# bfs로 하고 맨해튼 > 2 이면 1 없으면 0으로 하면 되는듯 
# 2중은 오랜만이라 스트레스...
import collections
import copy

# main BFS
m, n = 5, 5

def boundary(i,j):
    return i >= 0 and j >= 0 and i <= n - 1 and j <= m - 1
      
def get_ij_indices(places):
    i_indices = []
    j_indices= []
    for i, place in enumerate(places):
        for j, p in enumerate(list(place)):
            if p == 'P':
                i_indices.append(i)
                j_indices.append(j)
    return i_indices, j_indices

direction = [[1,0], [-1,0], [0,1], [0,-1]]

depth = 0
def main(place): 
    i_indices, j_indices = get_ij_indices(place)
    q = collections.deque()
    visited = {}
    for i in range(len(i_indices)):
        q.append([0, i_indices[i], j_indices[i], i])
        visited[i] = [[0 for _ in range(n)] for __ in range(m)]
        visited[i][i_indices[i]][j_indices[i]] = 1
    while len(q):
        depth, i, j, ith = q.popleft()
        for d in direction:
            if boundary(i + d[0], j + d[1]) and visited[ith][i + d[0]][j + d[1]] == 0:
                if place[i + d[0]][j + d[1]] == 'P':
                    print(i + d[0], j + d[1])
                    if depth <= 1:
                        return 0
                if place[i + d[0]][j + d[1]] == 'O':
                    q.append([depth + 1, i + d[0], j + d[1], ith])
                    visited[ith][i + d[0]][j + d[1]] = 1
    return 1
               

def solution(places):
    return [main(place) for place in places]
