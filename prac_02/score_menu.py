MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit
"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("enter score: "))
            if score < 0 or score > 100:
                print("invalid score!")
            else:
                print(MENU)
                choice = input(">>> ").upper()
        elif choice == "P":
            print(grade_result(score))
            print(MENU)
            choice = input(">>> ").upper()
        elif choice == "S":
            print(show_stars(score))
            print(MENU)
            choice = input(">>> ").upper()
        else:
            print("Invalid choice")
            print(MENU)
            choice = input(">>> ").upper()
    print("Farewell")


def grade_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def show_stars(score):
    stars = score
    for z in range(stars):
        print("*", end='')


main()
