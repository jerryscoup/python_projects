"""Write a program that prints the block letter “B” in a 7 × 6 grid of stars."""
for i in range(7):
    if i==0 or i==3 or i==6:
        print("*****")
    else:
        print("*     *")   
        