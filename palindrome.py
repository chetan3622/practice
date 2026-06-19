n = input("Enter number to check palindrome: ")
if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
