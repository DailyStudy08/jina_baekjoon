scene=1
while True:
    n = int(input())
    if n == 0:
        break
    student = [input() for _ in range(n)]
    list=[]
    for i in range(2*n - 1):
        num= int(input().split()[0])
        if num in list:
            list.remove
        else:
            list.append(num)

    count = len(list)
    for i in range(count):
        for num in list:
            print(scene, student[num-1])
    scene=scene+1