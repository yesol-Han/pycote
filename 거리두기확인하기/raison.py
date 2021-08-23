def solution(places):
    answer = []

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 4 방향 탐색 2번 , 거리두기 준수했으면 1, 아니면 0

    for place in places:
        flag = 1
        visit_lst = [[0] * 5 for __ in range(5)]

        for i in range(5):
            for j in range(5):

                if place[i][j] == 'P' and visit_lst[i][j] == 0:
                    visit_lst[i][j] = 1

                    for r in range(4):
                        x = i + dx[r]
                        y = j + dy[r]

                        if -1 < x < 5 and -1 < y < 5:
                            if place[x][y] == 'P' and visit_lst[x][y] == 0:
                                flag = 0
                            elif place[x][y] == 'O':

                                for t in range(4):
                                    q = x + dx[t]
                                    w = y + dy[t]
                                    if -1 < q < 5 and -1 < w < 5:
                                        if place[q][w] == 'P' and visit_lst[q][w] == 0:
                                            flag = 0

        answer.append(flag)

    return answer