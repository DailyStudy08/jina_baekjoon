import sys
n = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
search = list(map(int,sys.stdin.readline().split()))

dic=dict()

for c in card:
    if c in dic:
        dic[c]+=1
    else:
        dic[c]=1

for i in range(m):
    if search[i] in dic:
        print(dic[search[i]],end=' ')
    else:
        print(0, end=' ')

