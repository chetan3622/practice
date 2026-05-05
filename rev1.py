n=98970
rev=''
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
print('the reverse of the number is',rev)