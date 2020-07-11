def persistence(n):
    counter = 0
    while len(str(n)) > 1:
        counter += 1
        new_n = 1
        dig = [int(x) for x in str(n)]
        for i in dig: new_n *= i
        n = new_n
    return counter
