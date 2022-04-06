import random

LOW = 1
HIGH = 45
LINE = 6


def main():
    choice = get_valid_input()
    for choice in range(choice):
        print(" ".join("{:2}".format(x) for x in generate_random_numbers()))
    print()


def get_valid_input():
    """Prevent input error"""
    num = int(input("How many quick picks? "))
    while num < 0:
        print("That's not possible.")
        num = int(input("How many quick picks? "))
    return num


def generate_random_numbers():
    numbers = []
    for x in range(LINE):
        rdm_number = random.randint(LOW, HIGH)
        while rdm_number in numbers:
            rdm_number = random.randint(LOW, HIGH)
        numbers.append(rdm_number)
    numbers.sort()
    return numbers


main()
