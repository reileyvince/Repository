#F = C x 9/5 + 32
#C = F - 32 / 1.8

a = input("Would you like me to convert to celsius or fahrenheit? ")

if a == "celsius":
    b = int(input("Please input the number in fahrenheit "))
    c = b - 32 / 1.8
    print(b, "converted into celsius is", c)

elif a == "fahrenheit":
    d = int(input("Please input the number in celsius " ))
    e = d * 9 / 5 + 32
    print(d, "converted into fahrenheit is", e)
