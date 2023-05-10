
from guitar import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()

    for line in in_file:

        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)

    in_file.close()

    out_file = open('guitars.csv', 'a')

    name = input("Guitar name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        print(f"{name} ({year}) : ${cost:.2f} added")
        guitars.append(Guitar(name, year, cost))
        name = input("Guitar name: ")

    for guitar in guitars:
        print(guitar)

    for guitar in guitars:
        out_file.write(f'{guitar}')


main()
