n,m=map(int,input().split())

board=[[]*m for _ in range(n)]
for i in range(n):
    for i in range(m):
        board[n][m]=input()

# board=[]
# for _ in range(n):
#     board.append(input())

count=[]
for i in range(n-7):
    for j in range(m-7):
        black=0
        white=0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y)%2==0: 
                    if board[x][y] =='B':
                        white+=1
                    else:
                        black+=1
                else:
                    if board[x][y]=='B':
                        black+=1
                    else:
                        white+=1
        count.append(black)
        count.append(white)
print(min(count))



