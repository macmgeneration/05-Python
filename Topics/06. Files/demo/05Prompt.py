import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

fname = input('Enter the file name: ')
fhand = open(path + '/' + fname)
    
counter = 0
for line in fhand:
    if line.startswith('Subject:') :
        counter += 1
fhand.close()

print('There were ', counter, 'subject lines in', fname)