t=int(input())
for i in range(t):
    scores=list(map(int,input().split()))
    scores=scores[1:]
    avg=sum(scores)/len(scores)
    count=0
    for score in scores:
        if score>avg:
            count=count+1
    result=count/len(scores)*100
    print(f'{result:.3f}%')