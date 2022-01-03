fname= input("Enter the file name: ")
fh= open(fname)
words= []
fwords= []
for line in fh:
    line = line.strip()
    words=line.split()
    for w in words:
        if fwords.count(w) > 0:
            continue
        else:
            fwords.append(w)
fwords.sort()
print(fwords)
