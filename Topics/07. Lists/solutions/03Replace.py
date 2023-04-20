def replace(s, old, new):
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i].replace(old, new)
    return " ".join(words)

assert(replace('Mississippi', 'i', 'I') == 'MIssIssIppI')

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
assert(replace(s, "om", "am") ==
"I love spam! Spam is my favorite food. Spam, spam, yum!")
assert(replace(s, "o", "a") ==
"I lave spam! Spam is my favarite faad. Spam, spam, yum!")