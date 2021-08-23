

# 성공적으로 수행한다 -> 모든 문자열이 스택에 들어갔다가 조건에 맞춰 pop됨
# 스택에 문자열이 남아있다면 실패 -- > return 0

def solution(s):
    stack = []

    for alpha in s:
        if stack:
            if alpha == stack[-1]:
                stack.pop()
            else:
                stack.append(alpha)
        else:
            stack.append(alpha)

    if stack:
        return 0
    else:
        return 1