N=int(input())
stack=[]
result=[]
cnt=1
for _ in range(N):
    n=int(input())
    while cnt <= n :
        stack.append(cnt)
        cnt+=1
        result.append('+')
    if n==stack[-1]:
        stack.pop()
        result.append('-')

if not stack:
    print('\n'.join(result))
else:
    print('No')
        
    