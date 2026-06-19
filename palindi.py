n=8998
origin=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if origin==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
