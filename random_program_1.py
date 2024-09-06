""""Suppose a five digit number is entered through the keyboard. Write a program to separate each digit, add 48 to each digit and calculate the sum."""

num=int(input("please enter a five digit number:"))
if((9999<num) and (num<100000)):
    a=num//10000
    b=num//1000 - a*10
    c=num//100 - a*100 - b*10
    d=num//10 - a*1000 - b*100 - c*10
    e=num//1- a*10000 - b*1000 - c*100 - d*10
    sum=0
    array=[a,b,c,d,e]
    for i in range(5):
        sum= sum+array[i]+48
    print("the sum of the numbers is",sum)    
    

else:
    print("enter number does not satisfy above 5 digit number rule")
