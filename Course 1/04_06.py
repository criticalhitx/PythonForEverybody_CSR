def computepay(h,r):
    if(hrs>40):
        pay=40*r+(h-40)*r*1.5
    else:
        pay=h*r
    return pay

hrs = input("Enter Hours:")
rph = input("Enter Rate:")

try:
    hrsf=float(hrs)
    rphf=float(rph)
except:
    print("Input Error")
    exit()

p = computepay(hrsf,rphf)
print("Pay",p)