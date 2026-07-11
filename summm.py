n=int(input('enter a number'))
sum=0
while n > 0:
    num=num%10
    sum=sum*10+num
    n=n//10
print(sum)
