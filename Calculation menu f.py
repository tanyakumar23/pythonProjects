from math import pi, sqrt, pow
print("Enter  1 to find Area of Circle")
print("Enter 2 to find Diagonal of Square")
print("Enter 3 to find Area of Square")
number = int(input())

value = int(input("Enter value:"))

if number == 1:
    print("Area of Circle: ", pi*pow(value,2) )
elif number == 2:
    print("Diagonal of Square: ", sqrt(2)*value)
elif number == 3:
    print("Area of Square: ", pow(value,2))