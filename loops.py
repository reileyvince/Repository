#First line is to ask user for a variable
n = int(input("Please input a non negative integer "))
f = 1

#The loop creates the numbers inbetween 1 and the variable
for i in range(1, n +1):
    f = f * i
    print(i,":",f)
#If negative is entered, program will end 
if n < 0:
    print("You did not input a non negative integer")
    quit()
    
