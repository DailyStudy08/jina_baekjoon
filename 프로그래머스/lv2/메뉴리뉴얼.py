import itertools 
from itertools import combinations 

orders=["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course=[2,3,5]


def solution(orders,course):
    all=dict()
    for order in orders:
        n=len(order)
        if n<course[0]:
            continue
        for c in course:
            order=list(order)
            order.sort()
            temp=list(combinations(order,c))
            for t in temp:
                t=''.join(t)
                all[t]=all.get(t,0)+1


    #코스, 주문개수
    all = [(key,value) for key,value in all.items() if value>=2]
    all.sort(key=lambda x:-x[1])

    answer=[]
    for cnt in course:
        max_order=0
        for d in all:
            d_order=d[1]
            d_len = len(d[0])
            if d_len==cnt:
                if d_order>=max_order:
                    max_order=d_order
                    if d[0] not in answer:
                        answer.append(d[0])
    answer.sort()

    return answer
solution(orders,course)
