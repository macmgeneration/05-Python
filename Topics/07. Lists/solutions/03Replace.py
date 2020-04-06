def replace(s, old, new):
    while True:
        if old in s:
            s = s.replace(old, new)
        else:
            break
    return s

assert(replace('Mississippi', 'i', 'I') == 'MIssIssIppI')

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
assert(replace(s, "om", "am") ==
"I love spam! Spam is my favorite food. Spam, spam, yum!")
assert(replace(s, "o", "a") ==
"I lave spam! Spam is my favarite faad. Spam, spam, yum!")