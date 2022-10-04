k=int(input())
arr=[]
for i in range(k) :
    n=int(input())
    if n==0:
        arr.pop()
        continue
    else:
        arr.append(n)
print(sum(arr))