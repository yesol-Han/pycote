def solution(s):
    answer = []

    s = s.replace('{', '')
    s = s.replace('}', '')

    s_lst = s.split(',')
    word_dict = {}
    for word in s_lst:

        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sort_word_dict = sorted(word_dict.items(), key=lambda x: -x[1])
    for i in sort_word_dict:
        answer.append(int(i[0]))

    return answer