"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = get_valid_input()
    print(determine_category(score))


def get_valid_input():
    value_input = False
    while not value_input:
        try:
            num = float(input("Enter score: "))
            value_input = True
            return num
        except:
            print("Enter a valid input.")


def determine_category(num):
    if num < 50:
        return "Bad"
    elif 50 <= num < 90:
        return "Passable"
    else:
        return "Excellent"


main()

