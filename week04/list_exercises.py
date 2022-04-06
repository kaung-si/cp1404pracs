numbers = []


def main():
    for x in range(5):
        num = int(input("Number: "))
        numbers.append(num)
    print("The first number is {}"
          "The last number is {}"
          "\nThe smallest number is {}"
          "\nThe largest number is {}"
          "\nThe average of the numbers is {}"
          .format(numbers[0], numbers[-1], min(numbers), max(numbers), sum(numbers) / len(numbers)))


main()
