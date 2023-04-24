import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
import pathlib

MAX_DEPTH = 2
url_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

def ExtractUrls(url, urls, depth):
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError:
        return
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    for tag in tags:
        link = tag.get('href', None)
        if re.search(url_pattern, link):
            urls.append(link)
            if depth < MAX_DEPTH:
                ExtractUrls(link, urls, depth + 1)

path = str(pathlib.Path(__file__).parent.absolute())

web = input('Entrer a web: ')

try:
    urls = list()
    ExtractUrls(web, urls, 0)

    with open(path + '/hrefsrec.txt', 'w') as fsave:
        for tag in urls:
            fsave.write('\n'.join(urls))
except ValueError:
    print('The web address entered is not correct')