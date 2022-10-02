n=int(input())
p=[]
for _ in range(n):
    x,y=map(int,input().split())
    p.append((x,y))
for i in range(n):
    x,y=p[i]
    rank=1
    for j in range(n):
        a,b=p[j]
        if x<a and y<b:
            rank+=1
    print(rank,end=' ')