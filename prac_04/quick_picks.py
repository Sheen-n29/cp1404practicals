import random

NUM_PER_LINE = 6
MIN_VALUE = 1
MAX_VALUE = 45


get_quick_picks = int(input("How many quick picks? "))

for i in range(get_quick_picks):
    quick_picks = []
    for x in range(NUM_PER_LINE):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        while number in quick_picks:
            number = random.randint(MIN_VALUE, MAX_VALUE)
        quick_picks.append(number)
    quick_picks.sort()
    print(" ".join(f"{number:2}" for number in quick_picks))
