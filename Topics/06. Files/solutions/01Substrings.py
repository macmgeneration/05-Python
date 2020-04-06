import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

fname = input('Enter the file name: ')
try:
    fopen = open(path + '/' + fname, 'r', encoding="utf-8")
except:
    print('File ', fname, ' not found')
    quit()

search = input('Enter text to search: ')
if search == '':
    quit()

counter = 0
for line in fopen:
    if search in line:
        print(line.strip())
        counter += 1

print('Found ' + search + ' ' + str(counter) + ' times')
fopen.close()
