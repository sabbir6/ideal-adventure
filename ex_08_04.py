fhandle=input("Enter the name: ")
try:

    fopen=open(fhandle)
except:
    print("File doesn't exist: ",fhandle)
    quit()    
lst=list()
for line in fopen:
    line = line.rstrip()
    words=line.split()
    for word in words:
     
     if word not in lst:
      lst.append(word) 
     else:continue   
lst.sort()
print(lst)

       
