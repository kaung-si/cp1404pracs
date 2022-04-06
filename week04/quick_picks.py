import random

LOW = 1
HIGH = 45
LINE = 6


def main():
    """Iterate a line of random numbers for input times"""
    choice = get_valid_input()
    for choice in range(choice):
        print(" ".join("{:2}".format(x) for x in generate_random_numbers()))
    print()


def get_valid_input():
    """Prevent integer 0 input"""
    num = int(input("How many quick picks? "))
    while num < 0:
        print("That's not possible.")
        num = int(input("How many quick picks? "))
    return num


def generate_random_numbers():
    """Create a list of non-repetitive random numbers between LOW and HIGH"""
    numbers = []
    for x in range(LINE):
        rdm_number = random.randint(LOW, HIGH)
        while rdm_number in numbers:
            rdm_number = random.randint(LOW, HIGH)
        numbers.append(rdm_number)
    numbers.sort()
    return numbers


main()
