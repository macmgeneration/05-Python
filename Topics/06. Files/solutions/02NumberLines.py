import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

fname = input('Enter the file name: ')
try:
    fopen = open(path + '/' + fname, 'r')
except:
    print('File ', fname, ' not found')
    quit()

ext = pathlib.Path(fname).suffix
fsavename = pathlib.Path(fname).stem + 'Numbered' + ext

fsave = open(path + '/' + fsavename, 'w')
counter = 1
for line in fopen:
    line = str(counter).zfill(4) + ' ' + line
    #line = '{0:04d} {1}'.format(counter, line)
    fsave.write(line)
    counter += 1

print('File ' + fsavename + ' generated')

fsave.close()
fopen.close()
