"""written by jerryscoup
aim of the code is to output the gross salary of the working employee by inputing basic terms like hra da by the user
Accept the basic salary of an employee through the keyboard. HRA is 30% of basic salary and DA is 60% of basic salary and other allowances are 40% of basic salary. Write a program to calculate the gross salary. """
#basic_pay=basic salary
#DA= dearness allowance
#HRA=house rent allowance
print("to find the gross salary of employees")
basic_pay=float(input("enter the basic salary of the employee:"))
HRA=(basic_pay//100)*30
DA=(basic_pay//100)*60
other_allowance=(basic_pay//100)*40
print("HRA:",HRA,"\nDA :",DA,"\nother_allowances :", other_allowance)
gross_salary=basic_pay+HRA+DA+other_allowance
print("the gross salary is :",gross_salary)