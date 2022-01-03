import xml.etree.ElementTree as et
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url= input('Enter the URL: ')
html = urllib.request.urlopen(url).read()
tree= et.fromstring(html)
bra = tree.findall('comments/comment')
numl=[]
for i in bra:
     num= int(i.find('count').text)
     numl.append(num)
print('Total: ', sum(numl))
