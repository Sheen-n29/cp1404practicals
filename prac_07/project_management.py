
import datetime
from project import Project

FILE = "projects.txt"


def main():

    projects = []
    in_file = open(FILE, 'r')
    in_file.readline()

    with open(f"{project_name}", "r") as f:
        next(f)
        for line in f:
            name, start_date, priority, estimate, completion = line.strip().split("\t")
            projects.append(Project(name, start_date, int(priority), float(estimate), int(completion)))

    print(projects)

    print(projects)
    print("- (L)oad projects \n- (S)ave projects \n- (D)isplay projects \n- (F)ilter projects by date \n- (A)dd new project \n- (U)pdate project \n- (Q)uit")
    menu_select = input(">>> ").upper()

    while menu_select != "Q":
        if menu_select == "L":
            print("L")
        elif menu_select == "S":
            print("S")
        elif menu_select == "D":
            print("D")
        elif menu_select == "F":
            print("F")
        elif menu_select == "A":
            print("A")
        elif menu_select == "U":
            print("U")
        else:
            print("Invalid Input")
        menu_select = input(">>> ").upper()


main()
