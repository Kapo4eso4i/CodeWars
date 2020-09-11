def primes(low, hight):
    result = []
    for i in range(low, hight+1):

        for x in range(2, i):
            if (i % x) == 0:
                break
        else:
            result += [i]
    return result


print(primes(3, 1000))