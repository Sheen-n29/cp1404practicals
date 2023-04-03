numbers = []
for i in range(5):
    get_number = int(input("Number: "))
    numbers.append(get_number)
print(f'the first number is {numbers[0]}')
print(f'the last number is {numbers[-1]}')
print(f'the smallest number is {min(numbers)}')
print(f'the largest number is {max(numbers)}')
print(f'the average of the numbers is {sum(numbers)/5}')

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
get_username = input("Enter username: ")
if get_username in usernames:
    print("Access granted")
else:
    print("Access denied")
