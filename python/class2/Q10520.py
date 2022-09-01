t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    #층수, 각층의방수, 몇번째손님
    num = n//h+1
    floor = n%h
    if n%h==0:
        num=n//h
        floor=h
    print(f'{floor*100+num}')