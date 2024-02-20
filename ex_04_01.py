def computepay(hours,rate):
    if hours > 40:
         
        rep=hours*rate
        otp=(hours-40)*(rate*0.5)
        pay=rep+otp
    else :
        pay=hours*rate
    return pay

xh=input("Enter Hour: ")
xr=input("Enter Rate: ")
fh=float(xh)
fr=float(xr)

xp=computepay(fh,fr)
print("pay:",xp)
