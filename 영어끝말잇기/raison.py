def solution(n, words):
    check_dict = {}
    idx, order = 0, 1
    flag = 0
    last_word = []

    for word in words:

        idx += 1
        if idx == n + 1:  # 번호와 순서를 정한다
            idx = 1
            order += 1

        if last_word:  # 비교할 단어가 있다면
            """
            지금 말한 단어가 check_dict에 없고 단어 첫번째 글자가 last_word랑 같다면
            """
            if word not in check_dict and word[0] == last_word:

                check_dict[word] = 1
            else:
                flag = 1
                break
        else:  # 비교할 단어가 없다면 , 즉 첫번째 단어면
            check_dict[word] = 1

        last_word = word[-1]

    if flag == 0:
        return [0, 0]
    else:
        return [idx, order]