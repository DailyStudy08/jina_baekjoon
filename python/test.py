def ex(num):
    if num < 2:
        print(num,end='')
    else:
        ex(num//2)
        print(num%2,end='')

ex(20) #10100
print()
ex(10) #1010
print()
ex(5) #101
print()
ex(2) #10
print()
ex(1) #1