def disemvowel(string):
    string_new = []
    for letter in string:
        if letter in "euioaEUIOA":
            continue
        string_new.append(letter)
    return "".join(string_new)


# And correct one
def disemvowel_cor(string):
    return string.translate(str.maketrans('', '', "euioaEUIOA"))
