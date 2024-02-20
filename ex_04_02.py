def computegrade(score):
    if score>=0.9 and score<=1 :
        c='A'
        return c

    elif  score>=0.8 and score<0.9 :
        c='B' 
        return c

    elif score>=0.7 and score<0.8 :
        c='C'
        return c

    elif score>=0.6 and score<0.7 :
        c='D'
        return c  
    elif score<0.6 and score>=0 :
        c="F"
        return c
    else:
        return "Bad score"
    return 
sc=input("Enter score: ")
try:
    s=float(sc)
except:
    print("Bad score") 
    quit()   

grade=computegrade(s)
print(grade)
   