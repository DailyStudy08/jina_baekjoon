import sys
N = int(sys.stdin.readline())
que=[]
def push():
    pass

for _ in range(N):
    com = cmd = sys.stdin.readline().split()
    if com[0]=='push':
        que.append(int(com[1]))
    elif com[0]=="pop":
        if not que:
            print(-1)
        else:
            print(que.pop(0))
    elif com[0]=='size':
        print(len(que))
    elif com[0]=='empty':
        if not que:
            print(1)
        else:
            print(0)
    elif com[0]=='front':
        if not que:
            print(-1)
        else:
            print(que[0])
    elif com[0]=='back':
        if not que:
            print(-1)
        else:
            print(que[-1])

