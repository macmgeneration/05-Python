def analize(s):
    s = s.replace('áéíóú', '')
    words = s.split()
    count = 0
    for word in words:
        if word.count('e') > 0 :
            count += 1
    return (s, words, count)

text = "[CHANGEME]"
text, word, counter = analize(text)
print('Your text contains ', len(word), 'words, of which ',counter ,' (',counter / len(word) * 100 ,'%) contain an "e".')
