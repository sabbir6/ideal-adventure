fname=input('Enter the file name: ')
if len(fname) < 1:
    fname = "mbox-short.txt"

count=0
try:
    fopen=open(fname)
except:
    print('File not found:',fname) 
    quit()
for i in fopen:
    i=i.rstrip()
    
    if i.startswith('From ')  :
         
         words=i.split()
         
         word=words[1]
         count=count+1
         print(word)
         
print("There were", count, "lines in the file with From as the first word")         