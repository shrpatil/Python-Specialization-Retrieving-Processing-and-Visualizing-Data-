fh= open ('mbox.txt')
hrlist=[]
counts= dict()
tlist=list()
for line in fh:
    line= line.strip()
    if line.startswith('From '):
        words= line.split()
        hours= words[5]
        hr= hours.split(':')
        hrlist.append(hr[0])
for h in hrlist:
    counts[h]= counts.get(h,0)+1

for k,v in counts.items():
    newtup= (k,v)
    tlist.append(newtup)
tlist = sorted(tlist)

for k,v in tlist:
    print(k,v)
