def presses(phrase):
    keypad =  ['1', 'abc2', 'def3',
               'ghi4', 'jkl5', 'mno6',
               'pqrs7', 'tuv8', 'wxyz9',
               ' 0', '*', '#']
    counter = 0
    phrase = phrase.lower()
    for char in phrase:
        for key in keypad:
            if char in key:
                for i in range(len(key)):
                    if char == key[i]:
                        counter += i+1
    return counter


