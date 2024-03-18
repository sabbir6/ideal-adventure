def chop(l):
    l.remove('a')
    l.remove(5)
    

def middle(s):
    del s[1:4]
    
letters=['a','b','c','d',5]
letters1=[1,2,3,4,'e']
x=chop(letters)
print(x)
print(letters)

print(middle(letters1))
print(letters1)