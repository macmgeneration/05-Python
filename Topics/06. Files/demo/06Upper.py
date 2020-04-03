import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

fname = input('Enter the file name: ')
try:
    fopen = open(path + '/' + fname, 'r')
except:
    print('File ', fname, ' not found')
    quit()

fsavname = input('Enter the file name to save: ')

fsave = open(path + '/' + fsavname, 'w')
for line in fopen:
    fsave.write(line.upper())
fsave.close()
fopen.close()
