n=int(input("Enter number: "))
for i in range(2,n):
    if n%i==0:
        print('not prime number')
        break
else:
    print('prime number')