hr = input("Enter the hours: ")
rt = input("Enter the rate: ")
hour =float(hr)
rate =float(rt)

def computepay(hour,rate):
    if hour>40.0:
        extr= hour - 40

        pay= 40 * rate
        expay= extr * rate * 1.5
        total= pay +expay
        return total
    else:
        pay = hour * rate
        return pay
gross_pay = computepay(hour, rate)
print ("Pay",gross_pay)
