tot=0
count=0

while  True :
    savl=input('Enter a number: ')
    if savl == 'done':
        break
    try:
        favl=float(savl)
    except:
        print('Invalid input')
        continue    
    #print(favl)
    tot=tot+ favl
    count=count+1
#print('ALL DONE')    
print(tot,count,tot/count)