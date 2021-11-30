"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    random_score = random.randint(0, 101)
    print(return_score(score))
    print("random score is " + str(random_score))
    print(return_score(random_score))


def return_score(score):
    if score < 0:
        return "Invalid Score"
    else:
        if score > 100:
            return "Invalid score"
        elif 50 <= score < 90:
            return "Passable"
        elif score >= 90:
            return "Excellent"
        if score < 50:
            return "Bad"


main()
