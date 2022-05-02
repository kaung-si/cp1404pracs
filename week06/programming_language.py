class ProgrammingLanguage:
    """Represent programming language object."""

    def __init__(self, name="", typing_type="", reflection=True, year=0):
        self.name = name
        self.type = typing_type
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.type, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        return self.type == "Dynamic"
