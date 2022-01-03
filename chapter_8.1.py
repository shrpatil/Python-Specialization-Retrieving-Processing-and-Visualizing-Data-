fname = input("Enter the file name: ")
fh= open(fname)
count= 0
words= []
for line in fh:
    if not line.startswith('From '):
        continue
    else:
        words= line.split()
        print(words[1])
        count= count+1
print("There were", count, "lines in the file with From as the first word"  )
