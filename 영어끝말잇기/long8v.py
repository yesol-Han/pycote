def solution(n, words):
    already = set()
    last_alpha = ''
    for idx, word in enumerate(words):
        if idx > 0 and (word[0] != last_alpha or word in already):
            if (idx + 1) % n:
                return [(idx + 1) % n, (idx // n) + 1 ]
            else:
                return [n, (idx // n) + 1]
        last_alpha = word[-1]
        already.update([word])
    return [0, 0]