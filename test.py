def primes(low, high):
    result = []
    for i in range(low, high+1):

        for x in range(2, i):
            if (i % x) == 0:
                break
        else:
            result += [i]
    return result


print(primes(3, 1000))
