# 못풀었습니다.. 너무 어렵네여

from collections import deque
up, down, left, right = [-1, 0], [1, 0], [0, -1], [0, 1]

q = deque()

def check(place):
    visit = [[0] * 5] * 5
    place = [list(i) for i in place]
    for i in range(5):
        for j in range(5):
            if (place[i][j] == "P") and (visit[i][j] != 1):
                visit[i][j] = 1
                for direction in [up, down, left, right]:
                    new_i, new_j = i + direction[0], j + direction[1]
                    if (0 <= new_i < 5) and (0 <= new_j < 5):
                        if visit[new_i][new_j] != 1:
                            if (place[new_i][new_j] == "P"):
                                return 0
                            elif place[new_i][new_j] == "X":
                                pass
                            elif place[new_i][new_j] == "O":
                                visit[new_i][new_j] = 1
                                for direction in [up, down, left, right]:
                                    new_i, new_j = new_i + direction[0], new_j + direction[1]
                                    if (0 <= new_i < 5) and (0 <= new_j < 5):
                                        if visit[new_i][new_j] != 1:
                                            if (place[new_i][new_j] == "P"):
                                                return 0
                                            else:
                                                pass


    return 1
