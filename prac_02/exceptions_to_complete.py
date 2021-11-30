"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        user_input = int(input("Please enter a number: "))
        result = user_input
    except ValueError:
        print("Please enter a valid integer.")
    print("Valid result is:", result)
