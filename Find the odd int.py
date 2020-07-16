def find_it(seq):
    for x in set(seq):
        if seq.count(x) % 2:
            return x
