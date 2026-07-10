n=int(input('enter a number'))
rev=0
for i in range(n):
    num=n%10
    rev=num*rev+10
    n=n/10
print(rev)