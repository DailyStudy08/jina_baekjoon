from sys import stdin
N=stdin.readline()
A=sorted(map(int,stdin.readline().split()))
M=stdin.readline()
search=map(int,stdin.readline().split())

def binary(s,A,start,end):
    if start > end:
        return 0
    n=(start+end)//2
    if s==A[n]:
        return 1
    elif s<A[n]:
        return binary(s,A,start,n-1)
    else:
        return binary(s,A,n+1,end)
for s in search:
    start=0
    end=len(A)-1
    print(binary(s,A,start,end))