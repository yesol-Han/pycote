def solution(n):
    answer = ''

    number_lst = ['4', '1', '2']
    while n >= 1:

        a, b = divmod(n, 3)
        n = n // 3

        if b == 0:
            n = n - 1

        answer = number_lst[b] + answer

    return answer