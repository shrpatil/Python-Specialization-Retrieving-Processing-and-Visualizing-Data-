fname = input("Enter the file name: ")
fh = open(fname)

for line in fh:
    line = line.strip()
    line = line.upper()
    print(line)
