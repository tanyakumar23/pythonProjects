n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("Number is divisible by both 3 and 5")
elif n % 3 == 0 and n % 5 != 0:
    print("Number is divisible by 3 only")
elif n % 5 == 0 and n % 3 != 0:
    print("Number is divisible by 5 only")
else:
    print("Number is neither divisible by 3 nor 5")