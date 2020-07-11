def high_and_low(numbers):
    num = [int(x) for x in numbers.split()]
    num.sort()
    return str(num[-1]) + ' ' + str(num[0])
