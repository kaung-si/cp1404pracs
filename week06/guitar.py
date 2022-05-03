class Guitar:
    """Represent guitar objects"""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of guitars."""
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def __lt__(self, other):
        """"""
        return self.year < other.year

    def get_age(self):
        """Get guitar age"""
        return 2020 - self.year

    def is_vintage(self):
        """Determine if guitar is vintage or not"""
        return self.get_age() >= 50
