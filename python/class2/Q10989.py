<<<<<<< HEAD
n=int(input())
lst=[0]*10001
for _ in range(n):
    lst[int(input())]+=1

lst=set(lst)
for i in range(len(lst)):
    if lst[i]!=0:
        print(lst[i])
=======
import sys

n = int(sys.stdin.readline())
dp = [0] * 10001

for _ in range(n):
    dp[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for _ in range(dp[i]):
        print(i)
>>>>>>> 568ffa4c13a06ddf0ca6c0084365648e13dd3e8a
