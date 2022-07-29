t=int(input())
for i in range(t):
    ox=input()
    result=0
    score=1
    for i in range(len(ox)) :
        if ox[i]=='X':
            score=0  
        elif i==0 and ox[i]=='O':
            score=1
        elif ox[i]=='O' and ox[i-1]=='O':
            score=score+1
        elif ox[i]=='O':
            score=1
        result+=score
    print(result)
    

