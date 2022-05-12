import random

from week08.car import Car


class UnreliableCar(Car):

    def __init__(self, car_type, fuel):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(car_type, fuel)
        self.reliability = random.uniform(1, 100)

    def drive(self, distance):
        """Drive the car a given distance.

                Drive given distance if car has enough fuel
                or drive until fuel runs out return the distance actually driven or on reliable condition.
                """
        if random.uniform(1, 100) >= self.reliability:
            return distance == 0
        distance_driven = super().drive(distance)
        return distance_driven
