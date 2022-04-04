# Questions
# 1. A ValueError occurs when input is literal string or a decimal number.
# 2. A ZeroDivisionError occurs when denominator is 0.
# 3. We can avoid the possibility of ZeroDivisionError by filtering the input using while loop.
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
