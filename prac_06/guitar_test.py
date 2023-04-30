
from prac_06.guitar import Guitar


def main():

    gibson_guitar = Guitar("Gibson L-5 CES", 1923, 16035.40)
    guitar_2 = Guitar("Another Guitar", 2014, 400.50)

    print(f"{gibson_guitar.name} get_age() - Expected 100. Got {gibson_guitar.get_age()}")
    print(f"{guitar_2.name} get_age() - Expected 9. Got {guitar_2.get_age()}")
    print(f"{gibson_guitar.name} is_vintage() - Expected True. Got {gibson_guitar.is_vintage()}")
    print(f"{guitar_2.name} is_vintage() - Expected False. Got {guitar_2.is_vintage()}")


main()
