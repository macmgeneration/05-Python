import pathlib

xfile = open(str(pathlib.Path(__file__).parent.absolute()) + '/mbox-short.txt')
for cheese in xfile:
    print(cheese)
