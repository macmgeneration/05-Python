def letter_counter(s):
    letters = dict()
    for c in s:
        c = c.lower()
        if c == ' ': continue
        letters[c] = letters.get(c, 0) + 1
    
    result = dict()
    for i in sorted(letters):
        result[i] = letters[i]
    return result

text = "ThiS is String with Upper and lower case Letters"
print(letter_counter(text))