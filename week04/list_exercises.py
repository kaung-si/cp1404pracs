numbers = []


def main():
    """Start Program"""
    for x in range(5):
        num = int(input("Number: "))
        numbers.append(num)
    print("The first number is {}"
          "The last number is {}"
          "\nThe smallest number is {}"
          "\nThe largest number is {}"
          "\nThe average of the numbers is {}"
          .format(numbers[0], numbers[-1], min(numbers), max(numbers), sum(numbers) / len(numbers)))


def main_extended():
    """Start Program"""
    value_input = False
    counter = 1
    while not value_input:
        num = int(input(f"Number {counter}: "))
        while num > 0:
            value_input = True
            numbers.append(num)
            counter += 1
            num = int(input(f"Number {counter}: "))
    print("The first number is {}"
          "The last number is {}"
          "\nThe smallest number is {}"
          "\nThe largest number is {}"
          "\nThe average of the numbers is {}"
          .format(numbers[0], numbers[-1], min(numbers), max(numbers), sum(numbers) / len(numbers)))


# main()
main_extended()
