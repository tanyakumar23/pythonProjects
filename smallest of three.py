n1 = int(input("Enter number one: "))
n2 = int(input("Enter number two: "))
n3 = int(input("Enter number three: "))

if n1 < n2 and n1 < n3 :
    print(n1,"is the smallest number")
elif n2 < n1 and n2 < n3:
    print(n2,"is the smallest number")
else:
    print(n3,"is the smallest number")

