lst=[]
for _ in range(9):
    lst.append(int(input()))
total_val =  sum(lst)
lst.sort()
for i in range(9):
    for j in range(i+1,9):
        if total_val-lst[i]-lst[j]==100:
            n1=lst[i]
            n2=lst[j]
            lst.remove(n1)
            lst.remove(n2)
            break
    if len(lst)<9:
        break
for l in lst:
    print(l)



