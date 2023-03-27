"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Ans. It will occur when the input is not a number (str)
2. When will a ZeroDivisionError occur?
Ans. It will occur when the denominator is equal to 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes you can change it so that the user must enter a non-zero denominator
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
