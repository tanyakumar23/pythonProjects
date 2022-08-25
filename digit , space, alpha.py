a = input("Enter something: ")

if a == " ":
    print("HI space")
elif a.isdigit() == True:
    print("HI digit")
elif a <= 'Z' and a >= 'A':
    print("HI alp")

