from string import ascii_lowercase as chars

def solve(s):
    count = 0
    vowels = 'aeiou'
    values = {chars[x]:x+1 for x in range(len(chars))}
    result = []
    for char in s:
        if char not in vowels:
            count += values[char]
        else:
            result.append(count)
            count = 0
    return max(result)
