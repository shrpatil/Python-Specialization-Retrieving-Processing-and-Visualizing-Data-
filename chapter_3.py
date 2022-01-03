hr = input("Enter the hours: ")
rt = input("Enter the rate: ")
hour =float(hr)
rate =float(rt)

if hour>40.0:
    extr= hour - 40

    pay= 40 * rate
    expay= extr * rate * 1.5
    print( pay + expay)
else:
    pay = hour * rate
    print(pay)
