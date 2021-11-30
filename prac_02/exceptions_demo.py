"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Ans. ValueError will occur when the numerator or denominator is not an int value

2. When will a ZeroDivisionError occur?
Ans. ZeroDivisionError will occur when the denominator value is entered as 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Ans. By using a while loop to correct the user input
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Denominator cannot be zero, please try again")
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
