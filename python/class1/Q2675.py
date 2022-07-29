t=int(input())
for i in range(t):
    n,str=input().split()
    result=''
    for s in str :
        result+=s*int(n)
    print(result)
