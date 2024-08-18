"""written by jerryscoup 
the purpose of this program is to make a simple program that will calculate compound interest when other values are inputeed by the user"""
print("program to output the compound interest on some principal amount p,over the years n and at the rate of r")
#p=principal amount
#n=no. of the years
#r=rate of interest
#si=simple interest
#ci=compound interest
#amt=total amount 
p=float(input("please enter a principal amount:"))
r=float(input("please enter the required rate of interest:"))
n=float(input("please enter the number of years "))
si=(p*r*n)/100
amt=p*((1+(r/100))**n)
ci=amt-p
print("the simple interest is:",si,"\nthe compound interest is:",ci,"\nthe amount with compound interest is:",amt)
