"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from week06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Jeep", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)
    print("{} {}, {}".format(my_car.car_type, my_car.fuel, my_car.odometer))
    print("{self.car_type} {self.fuel}, {self.odometer}".format(self=my_car))
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print("{} fuel: {}".format(limo.car_type, limo.fuel))
    limo.drive(115)
    print("{} odometer: {}".format(limo.car_type, limo.odometer))
    print(limo)


main()
