def dashatize(num):
    if not isinstance(num, int):
        return 'None'
    num = str(abs(num))
    return ''.join('-' + x + '-' if int(x) % 2 else x for x in num).replace('--', '-').strip('-')
