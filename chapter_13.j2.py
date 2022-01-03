import json
import urllib.request, urllib.parse, urllib.error

url= input('Enter the URL: ')
js = urllib.request.urlopen(url).read()
numl=[]
info= json.loads(js)
print("Count:",len(info["comments"]))
for i in info["comments"]:
    num=int(i["count"])
    numl.append(num)

print("Sum:",sum(numl))
