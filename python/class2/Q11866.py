n,k=map(int,input().split())
arr=list(i for i in range(1,n+1))
result=[]
while(arr):
    for i in range(k-1):
        arr.append(arr.pop(0))
    result.append(str(arr.pop(0)))

print('<',', '.join(result),'>',sep='')