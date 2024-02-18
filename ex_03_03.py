sc=input("Enter score: ")
try:
    s=float(sc)
except:
    print("Bad score") 
    quit()   
if s>=0.9 and s<=1 :
        x='A'
        print(x)

elif  s>=0.8 and s<0.9 :
    c='B' 
    print(c)

elif s>=0.7 and s<0.8 :
    c='C'
    print(c)

elif s>=0.6 and s<0.7 :
    c='D'
    print(c)  
elif s<0.6 and s>=0 :
        p="F"
        print(p)
else:
    print("Bad score")
    

   