NAME_FILE = "name.txt"
NUMBER_FILE = "numbers.txt"

# program 1: ask name via user input and output to file
out_name = (open(NAME_FILE, "w"))
name = input("Enter your name: ")
print(name, file=out_name)

out_name.close()

# program 2 gets name via file and outputs stored name
in_name = (open(NAME_FILE, "r"))
print(f'Your name is {in_name.read()}')

in_name.close()

# program 3 gets individual numbers with readline and adds them together
in_number = open(NUMBER_FILE, "r")
number_1 = int(in_number.readline())
number_2 = int(in_number.readline())
print((number_1 + number_2))

in_number.close()

# program 4 gets number of each line and adds in loop to give the total result
in_number = open(NUMBER_FILE, "r")
total_num = 0
for line in in_number:
    number = int(line)
    total_num += number
print(total_num)
in_number.close()
