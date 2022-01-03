import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url= input("Enter the link: ")
count= int(input("Enter the count: "))
pos= int(input("Enter the position: "))

ind=0
while ind <= count:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    newl=tags[pos-1].get('href',None)
    print("Retriving: ",url)
    url= str(newl)
    ind= ind+1
