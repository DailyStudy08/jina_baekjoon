k,n=map(int,input().split())
lans=[]
for _ in range(k):
    lans.append(int(input()))
right=max(lans)
left=1

while left <= right:
    cnt = 0
    mid = (left+right)//2
    for lan in lans:
        cnt +=(lan//mid)
    if cnt >= n :
        left = mid+1
    else:
        right=mid-1
print(right)