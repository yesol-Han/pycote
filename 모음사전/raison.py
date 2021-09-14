result = 0


def solution(word):
    def back(lst, target, cnt):
        global result

        check_dict[target] = result
        if cnt == 5:
            return
        for i in lst:
            q = target + i
            result += 1
            back(lst, q, cnt + 1)

    lst = ['A', 'E', 'I', 'O', 'U']
    target = ''
    check_dict = {}
    back(lst, target, 0)
    return check_dict[word]