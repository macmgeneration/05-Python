import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

fhand = open(path + '/mbox-short.txt')
for line in fhand:
    print(line)

fhand.close()
