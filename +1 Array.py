def up_array(arr):
    s =''
    for x in arr:
        if 0 <= x < 10:
            s += str(x)
        else:
            return None
    if len(s) > 0:
        dig = int(s) + 1
    else:
        return None
    return [int(x) for x in str(dig)]
