# https://programmers.co.kr/learn/courses/30/lessons/12981
# 한방에 통과~

from collections import defaultdict
def solution(n, words):

    if len(words)%n == 0:
        max_round = len(words)//n
    else:
        max_round = len(words)//n + 1
        
    pre_words = defaultdict(lambda : 0)
    last_charater = words[0][0]
    
    for round in range(max_round):
        for each_person_index in range(n):
            try:
                each_word = words[(round*n) + each_person_index]
                pre_words[each_word] += 1
            except:
                return [0, 0]
            
            if pre_words[each_word] != 1:
                return [each_person_index+1, round+1]
            
            if each_word[0] == last_charater:
                last_charater = each_word[-1]
                pre_words[each_word] += 1
            else:
                return [each_person_index+1, round+1]
    return [0,0]

if __name__ == "__main__":
    words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    n = 3
    print(solution(n, words))

    words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
    n = 5
    print(solution(n, words))

    words = ["hello", "one", "even", "never", "now", "world", "draw"]
    n = 2
    print(solution(n, words))