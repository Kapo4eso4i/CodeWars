def find_nb(m):
    result = 1
    counter = 1
    while result < m:
        counter += 1
        result += counter ** 3
    return counter if result == m else -1
