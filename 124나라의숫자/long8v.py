def solution(n):
    answer = []
    while n :
        if n % 3 != 0:
            answer += [n % 3]            
            n = n // 3
        else:
            answer += [4] 
            n = n // 3 - 1
    return ''.join(map(str, answer[::-1]))