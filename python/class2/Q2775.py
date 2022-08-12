T=int(input())

# def home(k,n):
#     people=0
#     if k==0:
#         people=n
#         return people
#     else:
#         for i in range(1,n+1):
#             people+=home(k-1,i)
#     return people

for i in range(T):
    k=int(input())
    n=int(input())
    # print(home(k,n))

    arr=[[i for i in range(1,n+1)] for _ in range(k+1)]#0층 사람
    for i in range(1,k+1): #k층 n호
        for j in range(1,n):
            arr[i][j]=arr[i][j-1]+arr[i-1][j]
    print(arr[k][n-1])
