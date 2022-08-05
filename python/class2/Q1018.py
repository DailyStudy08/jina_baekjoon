n,m=map(int,input().split())

board=[]
for _ in range(n):
    board.append(input())

count=[]
for i in range(n-7):
    for j in range(m-7):
        white=0 #첫칸이 흰색일때 변경횟수
        black=0 #첫칸이 검정일때 변경횟수
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y)%2==0:  
                    if board[x][y] !='W':
                        white+=1
                    else:
                        black+=1
                else:
                    if board[x][y] !='B':
                        white+=1
                    else:
                        black+=1
        count.append(black)
        count.append(white)
print(min(count))



