from week08.taxi import Taxi
taxi = Taxi('Prius 1', 100)
taxi.drive(40)
print(taxi)
print(f"Current fare: ${taxi.get_fare():.2f}")
taxi.start_fare()
# Taxi.price_per_km = 2.20  # refers to the class variable.
taxi.drive(100)
print(taxi)
print(f"After attempting to drive anouther 100km\nCurrent fare: ${taxi.get_fare():.2f}")

