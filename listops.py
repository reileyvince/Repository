#List is printed
list = [1,2,3,4,5,6,7,8,9,10]
for item in list:
    print(item)

#List is added together and then printed
n = sum(list)
print("The sum of the list is:", n)

#Prints the largest and smallest number in the list
l = max(list)
s = min(list)
print("The largest number in the list is:", l)
print("The smallest number in the list is:", s)

#Prints the list in reverse order using slicing
print("The list in reverse order is:", list[::-1])

#Prints the largest and smallest number in the list
l = max(list)
s = min(list)
print("The largest number in the list is:", l)
print("The smallest number in the list is:", s)
