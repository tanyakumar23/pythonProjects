a = int(input("Enter a number: "))

if a % 2 == 0 and a > 0:
    print(a, ' is even and is positive  ')
elif a % 2 == 0 and a < 0:
    print(a, " is even and is negative")
elif a % 2 != 0 and a > 0:
    print(a, ' is odd and is postive ')
else:
    print(a, " is odd and negative")


