from collections import deque


def solution(priorities, location):
    locate_stack = deque([i for i in range(len(priorities))]) # 문서 순서
    stack = deque(priorities) # 중요도
    cnt = 0

    while True:
        # 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
        priority = stack.popleft()
        locate = locate_stack.popleft()

        if not stack:  # 2, 5, 8 런타임 에러 : 스택이 비어있을때 max 값 뽑을수 없어서
            return cnt + 1

        if max(stack) > priority: # 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.

            stack.append(priority)
            locate_stack.append(locate)

        else: # 그렇지 않으면 J를 인쇄합니다.
            cnt += 1
            if locate == location:
                return cnt
