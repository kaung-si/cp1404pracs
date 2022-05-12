from week08.taxi import Taxi
from week08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
taxis = [Taxi("Pirus", 100), SilverServiceTaxi('Limo', 100, 2), SilverServiceTaxi('Hummer', 100, 4)]


def main():
    """Taxi Simulator Program"""
    # taxis = [Taxi("Pirus", 100), SilverServiceTaxi('Limo', 100, 2), SilverServiceTaxi('Hummer', 100, 4)]
    total_bill = 0
    current_taxi = None
    print("Let's drive")
    menu_choice = validate_menu_choice()
    while menu_choice != "q":
        if menu_choice == 'c':
            display_available_taxis(taxis)
            taxi_choice = get_valid_choice()
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == 'd':
            if current_taxi:
                current_taxi.drive(float(input("Drive how far? ")))
                trip_cost = current_taxi.get_fare()
                total_bill += trip_cost
                print("Your {} trip costs ${:.2f}".format(current_taxi.car_type, trip_cost))
            else:
                print("You need to choose a taxi before you can drive")
        print("Bill to date: ${:.2f}".format(total_bill))
        menu_choice = validate_menu_choice()
    print("Total trip cost: {:.2f}\n"
          "Taxis are now".format(total_bill))
    display_available_taxis(taxis)


def validate_menu_choice():
    print(MENU)
    choice = input(">>>").lower()
    while choice not in ['c', 'q', 'd']:
        print("Invalid menu choice")
        choice = input(">>>").lower()
    return choice


def display_available_taxis(vehicles):
    print("Taxi available:")
    for index, vehicle in enumerate(vehicles):
        print("{} - {}".format(index, vehicle))


def get_valid_choice():
    value_input = False
    while not value_input:
        try:
            choice = int(input("Choose Taxi: "))
            value_input = True
            return choice
        except ValueError:
            print("Incorrect input type.")


main()
