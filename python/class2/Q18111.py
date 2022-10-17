n,m,b=map(int,input().split())
mine = []
for _ in range(n):
    mine += list(map(int, input().split()))
max_h = max(mine)
min_h = min(mine)
ans=[]
for h in range(min_h,max_h+1):
    inven = b
    time = 0 
    for mi in mine:
        d = mi - h
        if d>0:
            inven += d
            time += 2*d
        else:
            d=-d
            inven -=d
            time += d
    if inven<0:
        break
    ans.append([time,h])
ans.sort(key=lambda x : (x[0], -x[1]))
print(*ans[0])