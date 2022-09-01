n=int(input())
lst=[0]*10001
for _ in range(n):
    lst[int(input())]+=1

lst=set(lst)
for i in range(len(lst)):
    if lst[i]!=0:
        print(lst[i])