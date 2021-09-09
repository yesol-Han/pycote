from ast import literal_eval

def sort_by_len(lst):
    lst.sort(key=len)
    
    return lst

def solution(s):
    answer = []
    
    s = literal_eval(s.replace("{", "[").replace("}", "]"))
    s = sort_by_len(s)
    
    
    for elem in s:
        for e in elem:
            if e not in answer:
                answer.append(e)
                break
    
    return answer