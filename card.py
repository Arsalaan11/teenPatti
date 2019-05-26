class Card:
    def __init__(self, value, suit):
        self._value = None
        self._suit = None
        self.set_suit(suit)
        self.set_value(value)

    def __str__(self):
        return '{} of {}'.format(self.get_value(), self.get_suit())

    def get_value(self):
        return self._value

    def get_suit(self):
        return self._suit

    def set_value(self, value):
        self._value = value

    def set_suit(self, suit):
        self._suit = suit

    def get_card(self):
        return self._value, self._suit
