a = 0
b = 1
n = int(input("enter a number: "))
for i in range(n):
    print(a)
    a, b = b, a + b