l=int(input())
s=list(map(int,input().split()))
n=int(input())

if n in s :
    print(0)
else:
    result=[]
    s.append(n)
    s.sort()
    i=s.index(n)
    if i==0:
        for x in range(1,n+1):
            for y in range(n,s[1]):
                if x<y:
                    result.append([x,y])
    else:
        for x in range(s[i-1]+1,n+1):
            for y in range(n,s[i+1]):
                if x<y:
                    result.append([x,y])
    print(len(result))