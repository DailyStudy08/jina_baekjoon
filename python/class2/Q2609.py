a,b=map(int,input().split())
num1=0
for n in range(1,a+1):
    if a%n==0 and b%n==0:
        num1=n
num2=a*b//num1
print(num1)
print(num2)