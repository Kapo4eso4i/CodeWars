def find_short(s):
    length = len(sorted(s.split(), key=len)[0])
    return length  # l: shortest word length
