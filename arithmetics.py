print("calculator to find sum, difference, product,quotient,remainder of two number")
num_1=int(input("enter the value of first number :"))
num_2=int(input("enter the value of the second number :"))
add= num_1 + num_2
diff=num_1-num_2
multiply=num_1 * num_2
quotient= num_1/num_2
remainder=num_1 % num_2
print()
l1=['sum','difference','product','quotient','remainder']
l2=[add,diff,multiply,quotient,remainder]
l3=['and','and','and','by','by']
for i in range(0,5):
    print(i+1,".The",l1[i],"of",num_1,l3[i],num_2,"is :",l2[i])
    print()
    

