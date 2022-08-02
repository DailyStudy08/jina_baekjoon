str=input()
str=str.upper()
result=[0]*26
for s in str:
    result[ord(s)-65]+=1
max=max(result)
if result.count(max)>1:
    print('?')
else :
    i=result.index(max)
    print(chr(65+i))
