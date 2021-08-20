def solution(n, words):
    answer = []
    people = 0
    seq = 0
    for idx,i in enumerate(words):
        if answer:
            if answer[-1][-1] != i[0]:
                people = idx % n # 몇번쨰 사람이 떨어졌는지
                seq = idx // n # 떨어진 사람이 몇번쨰에 떨어졌는지
                break
        if i not in answer:
            answer.append(i)
        else:
            people = idx % n
            seq = idx // n
            break
            
    if len(answer) == len(words):
        return [0,0]
    else:
        people = people + 1 # index이므로 +1 해줌
        seq = seq + 1 # index이므로 +1 
        return [people,seq]