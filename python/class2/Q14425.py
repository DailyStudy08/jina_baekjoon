n,m=map(int,input().split())
ex=dict()
count=0
for _ in range(n):
    ex[input()]=0
for _ in range(m):
    str=input()
    if str in ex:
        count+=1
print(count)