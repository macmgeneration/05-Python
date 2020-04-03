import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

fhand = open(path + '/mbox-short.txt')
counter = 0
for line in fhand:
    counter += 1

fhand.close()

print('Line Count: ', counter)
