n=int(input('enter a number'))
rev=0
while n>0:
    num=n%10
    rev=num+rev*10
    n=n//10
print(rev)