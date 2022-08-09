n=int(input())
for m in range(1,n+1):
    m_lst=list(map(int,str(m)))
    if sum(m_lst)+m == n:
        print(m)
        break
else:
    print(0)


