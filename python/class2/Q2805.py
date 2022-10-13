import sys
n,m =map(int,sys.stdin.readline().split())
trees=list(map(int,sys.stdin.readline().split()))
right = max(trees)
left = 1
while left <= right :
    mid = (left + right ) //2
    total = 0
    for tree in trees:
        if tree > mid:
            total+= (tree-mid)
        if total > m:
            break
    if total >= m :
        left = mid +1
    else :
        right = mid-1
print(right)
