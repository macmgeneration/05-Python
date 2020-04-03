import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

fhand = open(path + '/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

fhand.close()