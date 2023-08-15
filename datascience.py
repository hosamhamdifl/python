from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re

r = urllib.request.urlopen('https://analytics.usa.gov/').read()
soup = BeautifulSoup(r, "lxml")
print(type(soup))
print(soup.prettify()[:100])
for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.get_text())
print(soup.prettify()[0:1000])
print("-----------------------------------------------------")
for link in soup.findAll('a', attrs={'href': re.compile("http")}):
    print(link)
type(link)
# test_string = '123abc456789abc123ABC'
# pattern = re.compile(r'abc')
# m=pattern.finditer(test_string)
# for x in m:
#     print(x)
#     print(x.span(),x.start(),x.end())
#     print(x.group())
print("-----------------------------------------------------")
file = open("parsed_data.txt", "w")
for link in soup.findAll('a', attrs={'href': re.compile("^http")}):
    soup_link = str(link)
    print(soup_link)
    file.write(soup_link)
file.flush()
file.close()
