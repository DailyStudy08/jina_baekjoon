m=int(input())
n=int(input())
result=[]
for i in range(m,n+1):
    if i ==1 :
        continue
    if i==2:
        result.append(i)
    else:
        for j in range(2,i):
            if i%j==0:
                break
            if j==i-1:
                result.append(i)
if len(result)==0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
