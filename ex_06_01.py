str = 'X-DSPAM-Confidence: 0.8475'
postr=str.find(':')
print(postr)
picse=str.find(' ',postr)
print(picse)
exstr=str[picse+1:]
value=float(exstr)
print(value+1)

