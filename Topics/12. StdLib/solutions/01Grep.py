import pathlib
import re

path = str(pathlib.Path(__file__).parent.absolute())

while True:
    pattern = input('Enter a regular expression: ')
    if pattern == 'exit':
        break

    try:
        fhand = open(path + r'/../mbox.txt')
        try:
            counter = 0
            for line in fhand:
                if re.search(pattern, line):
                    counter += 1
            print('mbox.txt had {} lines that matched {}'.format(counter, pattern))
        except re.error:
            print('The pattern is not valid')
        finally:
            fhand.close()
    except FileNotFoundError:
        print('File mbox.txt not found')
        break
