def likes(names):
    length = len(names)
    if length > 3:
        answer = ", ".join(names[0:2]) + " and " + str(len(names) - 2) + " others like this"
    elif length == 3:
        answer = ", ".join(names[0:2]) + " and " + str(names[2]) + " like this"
    elif length == 2:
        answer = " and ".join(names[0:2]) + " like this"
    elif length == 1:
        answer = str(names[0]) + " likes this"
    else:
        answer = "no one likes this"
    return answer
