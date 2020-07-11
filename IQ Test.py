def iq_test(numbers):
    num_list = [int(x) for x in numbers.split()]
    odd_even = ['odd' if x % 2 else 'even' for x in num_list]
    return odd_even.index('even') + 1 if odd_even.count('even') == 1 else odd_even.index('odd') + 1
