N=int(input())
arr=[]
for i in range(N):
    age, name = input().split()
    age = int(age)
    arr.append((age,name))
arr.sort(key= lambda ddd : ddd[0])
for a in arr :
    print(a[0], a[1])