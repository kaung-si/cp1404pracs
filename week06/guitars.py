from week06.guitar import Guitar


def main():
    """Guitar Program"""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added")
        name = input("Name: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for index, guitar in enumerate(guitars):
            vintage_string = "(vintage)"[guitar.is_vintage()]
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(index + 1, guitar,
                                                                                      vintage_string))
    else:
        print("You have no guitar in list.")


main()
