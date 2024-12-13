file  = open ('students.txt', 'w')
file.write("Paul\nComputing: 50, 25\nNetworking: 60, 25\nDissertation: 70, 50")
file.close()

file = open('students.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line)
file.close()

file = open('results.txt', 'w')
file.write("\nPaul, 60, Merit")
file.close()

file = open('results.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line)
file.close()
