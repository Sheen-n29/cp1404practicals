out_file = open("name.txt", "w")

name = input("Please enter your name: ")
print("Your name is {}".format(name), file=out_file)
out_file.close()


in_file = open("name.txt", "r")

name = in_file.read()
First, Second, Third, Fourth = name.split()
in_file.close()
print("Your name is {}".format(Fourth))


in_file = open("numbers.txt", "r")
num_1 = int(in_file.readline())
num_2 = int(in_file.readline())
in_file.close()
sum = num_1 + num_2
print(sum)


in_file = open("numbers.txt", "r")
sum = 0
for line in in_file:
    num = int(line)
    sum += num
in_file.close()
print(sum)
