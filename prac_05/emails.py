email_and_name = {}
get_email = input("Email: ")


while get_email != "":
    split_email = get_email.split('@')[0]
    split_name = split_email.split('.')
    get_name = " ".join(split_name).title()

    confirm_name = input(f"Is your name {get_name}? y/n ").lower()

    if confirm_name == "n" or confirm_name == "no":
        corrected_name = input("Name: ")
        email_and_name.update({corrected_name: get_email})
    elif confirm_name == "y" or confirm_name == "yes" or confirm_name == "":
        email_and_name.update({get_name: get_email})

    get_email = input("Email: ")


for key in email_and_name:
    print(f'{key} ({email_and_name[key]})')
