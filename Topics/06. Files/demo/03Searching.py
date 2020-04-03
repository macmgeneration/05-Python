import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

fhand = open(path + '/mbox-short.txt')
for line in fhand:
    if line.startswith('From:') :
        print(line)

fhand.close()