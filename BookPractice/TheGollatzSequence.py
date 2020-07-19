def gollatz_seq(number):
    if number % 2:
        result = 3 * number + 1
    else:
        result = number // 2
    print(result)
    return result


try:
    u_number = int(input('Enter some number please: '))
    while u_number > 1:
        u_number = gollatz_seq(u_number)
except:
    print('Error: Invalid argument type!')

