n=int(input("Enter number: "))
a=0
b=1
while a <= n:
    if a==n:
        print("Fibonacci Number")
        break
    a,b=b,a+b
else:
    print("Not Fibonacci Number")