fname = input("Enter the file name: ")
fh = open(fname)
count=0
total = 0
for line in fh:
    line = line.strip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    fnum = line.find(' ')
    fval =float(line[fnum:fnum+7])
    total= total + fval
    count= count + 1
print ( "Average spam confidance:",total / count)    
