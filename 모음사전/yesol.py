def solution(word):
    answer = 0
    spell = ["Z", "A", "E", "I", "O", "U"]

    for zero in range(len(word), 5):
        word += "Z"

    for one in spell[1:]:
        for two in spell:
            for three in spell:
                if two == "Z" and three != "Z":
                    continue
                for four in spell:
                    if three == "Z" and four != "Z":
                        continue
                    for five in spell:
                        if four == "Z" and five != "Z":
                            continue

                        answer += 1
                        word_dict = one+two+three+four+five

                        if word == word_dict:
                            return answer
