import random

NUMBER_PER_LINE = 6
MAXIMUM = 45
MINIMUM = 1


def main():
    quick_picks = int(input("How many quick picks? "))

    while quick_picks < 0:
        print("Invalid entry please try again")
        quick_picks = int(input("How many quick picks? "))

    for i in range(quick_picks):
        quick_pick = []
        for x in range(NUMBER_PER_LINE):
            x += 1
            numbers = random.randint(MINIMUM, MAXIMUM)
            while numbers in quick_pick:
                numbers = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(numbers)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
