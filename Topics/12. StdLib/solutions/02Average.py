import pathlib
import re

path = str(pathlib.Path(__file__).parent.absolute())

pattern = r'^New Revision: ([0-9]+)'
try:
    file = input('Enter file (/../mbox-txt or /../mbox-short.txt): ')
    fhand = open(path + file)
    
    data = list()
    for line in fhand:
        find = re.findall(pattern, line)
        if len(find) > 0:
            data.append(int(find[0]))

    if len(data) == 0:
        print('Nothing')
    else:    
        print(int(sum(data) / len(data)))
    fhand.close()
except FileNotFoundError:
    print('File mbox.txt not found')
