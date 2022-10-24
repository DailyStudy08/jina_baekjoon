n,k=map(int,input().split())
v = [int(input()) for _ in range(n)]
total_cnt=0
i=n-1
while k>0:
    cnt=0
    cnt +=(k//v[i])
    k-=(v[i]*cnt)
    i-=1
    total_cnt+=cnt

print(total_cnt)