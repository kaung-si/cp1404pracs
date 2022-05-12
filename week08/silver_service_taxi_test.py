from week08.silver_service_taxi import SilverServiceTaxi
hummer = SilverServiceTaxi("Hummer", 100, 2)
print(hummer)
print("Total fare of {}km drive by {} is ${:.2f}".format(hummer.drive(18), hummer.car_type, hummer.get_fare()))
