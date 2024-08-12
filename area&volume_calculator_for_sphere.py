#written on aug 12 by puskarpuneet/jerryscoup
#purpose to write a program to calculate area and volume of sphere by taking radius as input from user
r=float(input("please enter radius of the sphere:"))#r=radius of the sphere
pi=3.14
#surface area= sa
#volume=vol
sa=4*pi*(r**2)
vol=(4/3)*pi*(r**3)
print("the surface area of the sphere is : ",sa)
print("the volume of the sphere is :",vol)