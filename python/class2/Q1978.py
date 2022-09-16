n=int(input())
lst=list(map(int,input().split()))
cnt=0

for l in lst:
    if l>1:
        if l==2:
            cnt+=1
        else:
            for i in range(2,l):
                if l%i==0:
                    break
            else:
                cnt+=1
print(cnt)
