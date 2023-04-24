import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

web = input('Entrer a web: ')

try:
    html = urllib.request.urlopen(web).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    with open(path + '/hrefs.txt', 'w') as fsave:
        for tag in tags:
            fsave.write(tag.get('href', None))
            fsave.write('\n')
except ValueError:
    print('The web address entered is not correct')