n=int(input("Enter a number: "))
rev=0
original=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if original==rev:
    print("The number is a palindrome.")    
else:    
    print("The number is not a palindrome.")