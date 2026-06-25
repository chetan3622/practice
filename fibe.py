n=int(input('enter a number'))
a=0
b=1
while a<n:
    c=a+b
    a=b
    b=c
if a==n:
    print('yes')
else:
    print('no')