import urllib.request, urllib.parse, urllib.error
import re
import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

web = input('Entrer a web: ')

url_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

try:
    with urllib.request.urlopen(web) as response:
        charset = response.info().get_content_charset()
        html = response.read().decode(charset)

        urls = re.findall(url_pattern, html)
        with open(path + '/urls.txt', 'w') as fsave:
            for url in urls:
                fsave.write(url)
                fsave.write('\n')
            #fsave.write('\n'.join(urls))  #compact version
except ValueError:
    print('The web address entered is not correct')