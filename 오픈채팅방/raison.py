def solution(record):
    answer = []
    id_dict = {}

    for i in record:
        k = i.split()
        if k[0] == 'Enter':
            id_dict[k[1]] = k[2]
        elif k[0] == 'Change':
            id_dict[k[1]] = k[2]

    for i in record:
        q = i.split()
        if q[0] == 'Enter':
            w = id_dict[q[1]] + '님이 들어왔습니다.'
            answer.append(w)
        elif q[0] == 'Leave':
            w = id_dict[q[1]] + '님이 나갔습니다.'
            answer.append(w)

    return answer