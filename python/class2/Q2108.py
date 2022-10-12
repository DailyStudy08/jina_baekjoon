from collections import Counter
import sys
m=int(sys.stdin.readline())
numbers=[]
for _ in range(m):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()
print(round(sum(numbers)/m))
print(numbers[m//2])

cnt = Counter(numbers).most_common() #빈도수 높은 2개
#[(-2, 2), (-1, 2), (-3, 1)] (값,빈도수)로 저장
if m==1:
    print(numbers[0])
else:
    if cnt[0][1]==cnt[1][1]: 
        print(cnt[1][0])
    else:
        print(cnt[0][0])
print(max(numbers)-min(numbers))