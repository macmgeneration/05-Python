import string

def analize(s):
    str = ""
    for c in s:
        if c not in string.punctuation : str += c
    words = str.split()
    count = 0
    for word in words:
        if 'e' in word :
            count += 1
    return (str, words, count)

text = """En un lugar de la Mancha, de cuyo nombre no quiero 
acordarme, no ha mucho tiempo que vivía un hidalgo de los de 
lanza en astillero, adarga antigua, rocín flaco y galgo corredor. 
Una olla de algo más vaca que carnero, salpicón las más noches, 
duelos y quebrantos los sábados, lantejas los viernes, algún 
palomino de añadidura los domingos, consumían las tres partes 
de su hacienda"""

text, word, counter = analize(text)
print (text)
print('Your text contains ', len(word), 'words, of which ', counter ,' (', round(counter / len(word) * 100, 2) ,'%) contain an "e".')
