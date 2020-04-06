import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

fname = input('Enter the file name: ')
try:
    fopen = open(path + '/' + fname, 'r')
except:
    print('File ', fname, ' not found')
    quit()

ext = pathlib.Path(fname).suffix
fsavename = pathlib.Path(fname).stem + 'Unnumbered' + ext

fsave = open(path + '/' + fsavename, 'w')
counter = 1
for line in fopen:
    search = str(counter).zfill(4) + ' '
    if line.startswith(search):
        line = line[5:]
    else:
        print('Pattern not found in line ' + str(counter))
        break
    fsave.write(line)
    counter += 1
else:
    print('File ' + fsavename + ' generated')

fsave.close()
fopen.close()
