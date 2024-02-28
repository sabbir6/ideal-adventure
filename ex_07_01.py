fhandle=open('mbox.txt')
#freading=fhandle.read()
#print(freading.upper())
count=0
sum=0
for line in fhandle:
    line=line.rstrip()
    if line.startswith('X-DSPAM-Confidence: '):
        
       
        
        fstr=line.find(':')
        value=line[fstr+1:]
        fvalue=float(value)
        count=count+1
        sum=sum+fvalue
       # print(line,count,fvalue,sum,sum/count)
print(sum/count)        