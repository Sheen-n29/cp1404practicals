
name = input("Enter name: ")
menu = """(H)ello
(G)oodbye
(Q)uit"""
print(menu)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
        print(menu)
        choice = input(">>> ").upper()
    elif choice == "G":
        print(f"Goodbye {name}")
        print(menu)
        choice = input(">>> ").upper()
    else:
        print("Invalid Choice")
        print(menu)
        choice = input(">>> ").upper()
print("Finished")


