class ValueObject:
    """
    Base class for value objects.  Provides equality based on attributes.
    """
    def __eq__(self, other):
        if other is None or type(self) != type(other):
            return False
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))