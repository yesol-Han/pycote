def solution(record):
    hash = {}
    for line in record:
        line = line.split(" ")
        if line[0] == "Enter":
            hash[line[1]] = line[2]
        elif line[0] == "Change":
            hash[line[1]] = line[2]
    
    answer = []
    for line in record:
        line = line.split(" ")
        if line[0] == "Enter":
            answer.append(hash[line[1]] + "님이 들어왔습니다.")
        elif line[0] == "Leave":    
            answer.append(hash[line[1]] + "님이 나갔습니다.")
        
    return answer