text = "X-DSPAM-Confidence:    0.8475"

lenght=len(text)
num1= text. find('0')
snum=float(text[num1:lenght+1])

print("Number: %f" % (snum))
