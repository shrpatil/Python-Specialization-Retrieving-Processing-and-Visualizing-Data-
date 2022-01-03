import re
fh= input("Enter file name: ")
fhandle= open(fh)
total=0
numl=[]
for line in fhandle:
    line = line.strip()
    lists = re.findall('([0-9]+)', line)
    if len(lists) == 0: continue
    i = len(lists)
    lists= list(int(x) for x in lists)
    numl= numl+lists
total= sum(numl)
print("There are",len(numl),"values")
print("Sum:",total)
