import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter Url: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

num=[]
tags = soup('span')
for tag in tags:
    t1= tag.contents[0]
    num.append(t1)

num= list(int(x) for x in num)
print('Total'sum(num))
