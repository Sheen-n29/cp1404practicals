def main():
    pass_length = get_password()
    while pass_length <= 4:
        print("Password must be at least 5 characters long")
        pass_length = get_password()
    print_asterisks(pass_length)


def print_asterisks(pass_length):
    for i in range(pass_length):
        print("*", end="")


def get_password():
    password = input("Please enter your password: ")
    pass_length = len(password)
    return pass_length


main()
