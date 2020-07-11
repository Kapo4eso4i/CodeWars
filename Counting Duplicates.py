def duplicate_count(text):
    counter = {}
    text = text.upper()
    for char in text:
        if text.count(char) > 1:
            counter[char] = 1
    return len(counter)

# Or we can do it by set/list comprehention:
#text = text.lower()
#len({char for char in set(text) if text.count(char) > 1})