from urllib.parse import urlparse, parse_qs
from lxml.html import fromstring
from requests import get
from os import system

system("clear")
system("figlet Dorking Tools | lolcat")
query = input ( 'input query : ' )

raw = get("https://www.google.com/search?q=" + query).text
page = fromstring(raw)

print ( 'Results: ' )

for result in page.cssselect(".r a"):
    url = result.get("href")
    if url.startswith("/url?"):
        url = parse_qs(urlparse(url).query)['q']
        print(url[0])

