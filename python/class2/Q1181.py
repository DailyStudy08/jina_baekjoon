n=int(input())
lst=[]
for _ in range(n):
    lst.append(input())
lst=list(set(lst))
lst.sort()
lst.sort(key=len)
for l in lst:
    print(l)