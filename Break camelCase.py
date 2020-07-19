def solution(s):
    for i in range(-1, len(s) - len(s)*2 -1, -1):
        if s[i].isupper():
            s = ' '.join((s[:i],s[i:]))

    return s
