from Assignment1 import card


class Player:
    def __init__(self, player_number):
        self._player_number = player_number
        self._hand = []
        self._rank_of_hand = 7

    def get_hand(self):
        return self._hand

    def get_rank(self):
        return self._rank_of_hand

    def set_rank(self, rank):
        self._rank_of_hand = rank

    def add_card_to_hand(self, the_card):
        if not isinstance(the_card, card.Card):
            raise ValueError('Only a Card can be added to a Hand')
        self._hand.append(the_card)

    @staticmethod
    def check_consecutive(list_to_check):
        return sorted(list_to_check) == list(range(min(list_to_check), max(list_to_check) + 1))

    def calculate_rank(self, deck_object):
        ace_sequence = [[0, 11, 12], [0, 24, 25], [0, 37, 38], [0, 50, 51],
                        [13, 11, 12], [13, 24, 25], [13, 37, 38], [13, 50, 51],
                        [26, 11, 12], [26, 24, 25], [26, 37, 38], [26, 50, 51],
                        [39, 11, 12], [39, 24, 25], [39, 37, 38], [39, 50, 51]]
        high_cards = [0, 10, 11, 12, 13, 23, 24, 25,
                      26, 36, 37, 38, 39, 49, 50, 51]
        hand = self.get_hand()
        reverse_lookup = deck_object.get_reverse_lookup_deck()
        values_to_deck_map = [reverse_lookup[the_card] for the_card in hand]
        values_of_hand = [the_card.get_value() for the_card in hand]
        suits_of_hand = [the_card.get_suit() for the_card in hand]
        if len(set(values_of_hand)) == 1:  # Three of same rank check
            self.set_rank(1)
        elif sorted(values_of_hand) in ace_sequence or self.check_consecutive(values_to_deck_map):
            if len(set(suits_of_hand)) == 1:  # Pure Sequence check
                self.set_rank(2)
            else:  # Sequence check
                self.set_rank(3)
        elif len(set(suits_of_hand)) == 1:  # Color Check
            self.set_rank(4)
        elif len(set(values_of_hand)) == 2:  # Pair check
            self.set_rank(5)
        elif not set(values_to_deck_map).isdisjoint(high_cards):  # High Card Check
            self.set_rank(6)
        else:
            self.set_rank(7)
        return self
