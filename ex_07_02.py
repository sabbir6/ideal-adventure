fname=input('Enter the file name : ')
count=0
try:
    ofile=open(fname)
    
    
except:
    print('File does not exist: ')
    quit()
sum=0    
for line in ofile :
    line=line.rstrip()
    if line.startswith('X-DSPAM-Confidence:') :
        
        count=count+1
        fstr=line.find(':')
        value=line[fstr+1:]
        fvalue=float(value)
        
        sum=sum+fvalue
       # print(line,count,fvalue,sum,sum/count)
print('Average spam confidence:',sum/count)        

          



