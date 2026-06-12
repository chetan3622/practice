n=int(input('enter a number:'))
a=0
b=1
while a <= n:
    if a==n:
        print('Fibonacci')
        break
    a,b=b,a+b
else:    
    print('Not Fibonacci Number')  
