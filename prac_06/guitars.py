from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        print(f"{name} ({year}) : ${cost:.2f} added")
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    print("These are my guitars:")

    for i, guitar in enumerate(guitars, 0):
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
