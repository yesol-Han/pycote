def solution(gems):
    answer = []
    gems_dict = {}
    #모든 보석의 종류를 뽑아온다
    for gem in gems:

        if gem not in gems_dict:
            gems_dict[gem] = 0

    L = len(gems_dict)

    start, end = 0, 0

    while end < len(gems):
        # 투포인터 알고리즘 사용

        if gems_dict[gems[end]] == 0:
            gems_dict[gems[end]] = -1
            L -= 1
        else:
            gems_dict[gems[end]] -= 1
        if L == 0:
            while L == 0:
                if gems[start] in gems_dict:
                    if gems_dict[gems[start]] == -1:
                        gems_dict[gems[start]] = 0
                        L += 1
                        answer.append([start + 1, end + 1, end - start + 1])
                    else:
                        gems_dict[gems[start]] += 1
                start += 1

        end += 1
    answer.sort(key=lambda x: (x[2], x[0]))
    return [answer[0][0], answer[0][1]]

gems = ["A","B","B","B","B","B","B","C","B","A"]
solution(gems)