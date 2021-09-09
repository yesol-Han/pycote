from collections import defaultdict
def solution(record):
    answer = []
    result = defaultdict(list)
    for i in record:
        i = i.split()
        if i[0] == 'Enter':
            result[i[1]] = i[2]
        elif i[0] == 'Change':
            result[i[1]] = i[2]
    
    for i in record:
        i = i.split()
        if i[0] == 'Enter':
            answer.append(str(result[i[1]]) + "님이 들어왔습니다.")
        elif i[0] == 'Leave':
            answer.append(str(result[i[1]]) + "님이 나갔습니다.")
    
    return answer