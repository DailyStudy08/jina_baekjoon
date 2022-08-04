l=int(input())
s=list(map(int,input().split()))
n=int(input())
s.sort()
num=0
list=[]
for i in range(len(s)) :
    if n > s[i] and n < s[i+1]:
        num=i

if num==0:
    print(0)
else:
    for x in range(s[num]+1,n):
        for y in range(s[num]+2,s[num+1]-1):
            if x<y:
                list.append([x,y])
    print(len(list))