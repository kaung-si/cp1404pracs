from week08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but with extra charge (flagfall)."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the silver service taxi trip."""
        return super().get_fare() + self.flagfall
