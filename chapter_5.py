
max_num = -1
min_num = None
while True:
    val = input('Enter Number:')
    if val == 'done':
        break
    try:
        num = int(val)
    except:
        print("Invalid input")
        continue
    if num > max_num:
        max_num = num
    else:
        if min_num is None:
            min_num = num
        elif min_num > num:
            min_num = num

print ("Maximum is", max_num)
print ("Minimum is", min_num)
