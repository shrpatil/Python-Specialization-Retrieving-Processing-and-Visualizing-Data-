fname = input("Enter the file name: ")
fh= open(fname)
eword=[]
words= []
counts= dict()
for line in fh:
    if not line.startswith('From '):
        continue
    else:
        words= line.split()
        eword.append(words[1])
for email in eword:
   counts[email]= counts.get(email,0)+1

bvalue=None
bkey= None
for k,v in counts.items():
    if bvalue is None or v > bvalue:
        bvalue= v
        bkey= k
print(bkey,bvalue)
