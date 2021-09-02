from collections import Counter
def solution(s):
    answer = []
    s=s.replace('{', '')
    s=s.replace('}', '')
    s=s.split(',')
    count_s=Counter(s)
    
    for i in count_s.most_common(): # 카운터가 많은 순서대로 뽑아준다.
        answer.append(int(i[0])) 
    return answer