def main():
    """Asks users for numbers and displays a variation of outputs"""
    numbers = []
    for i in range(5):
        get_num = int(input("Number: "))
        numbers.append(get_num)
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("THe average of the numbers is {}".format(sum(numbers) / len(numbers)))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    ask_user = input("Please enter your username: ")

    if ask_user in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


main()