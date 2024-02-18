xh=input("Enter Hour: ")
xr=input("Enter Rate: ")
fh=float(xh)
fr=float(xr)
if fh > 40:
    rp=fh*fr
    otp=(fh-40)*(fr*0.5)
    xp=rp+otp
else :
    xp=fh*fr

print("pay:",xp)
