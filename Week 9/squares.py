import math
accept = False
while(accept == False):
    n = int(input("Enter a number: "))
    try:
        math.sqrt(n)
        accept = True
    except ValueError:
        print("Please enter a positive number")

i = 0
while i**2<=n:
    if i % 2 == 0:
        print(i**2)
    i = i + 1
