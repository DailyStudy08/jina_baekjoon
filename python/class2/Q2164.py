import collections
import sys
n=int(sys.stdin.readline())
dque=collections.deque([i for i in range(1,n+1)])
while(len(dque)!=1):
    dque.popleft()
    dque.append(dque.popleft())
print(dque[0])
