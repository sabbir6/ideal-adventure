max_num=None
min_num=None

while True:
    sval=input('Enter a number: ')
    if sval=='done':
        break
    try:
        fval=float(sval)
    except:
        print('wright digit')
        continue
    
    if max_num == None or fval>max_num :
        
        max_num=fval
           
    if min_num==None or  fval<min_num:
        
        min_num=fval
       
          
        
print(max_num,min_num)        

        