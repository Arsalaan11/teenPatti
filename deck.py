import random
from Assignment1 import card
from Assignment1 import player


class Deck:
    def __init__(self):
        # Construct Deck
        self._deck = {}
        self._random_state = list(range(0, 52))
        for value in range(0, 52):
            if value < 13:
                suit = 'Hearts'
                splitter = 0
            elif 13 <= value < 26:
                suit = 'Spades'
                splitter = 13
            elif 26 <= value < 39:
                suit = 'Diamonds'
                splitter = 26
            else:
                suit = 'Clubs'
                splitter = 39
            if value in [0, 13, 26, 39]:
                self._deck[value] = card.Card('Ace', suit)
            elif value in [10, 23, 36, 49]:
                self._deck[value] = card.Card('Jack', suit)
            elif value in [11, 24, 37, 50]:
                self._deck[value] = card.Card('Queen', suit)
            elif value in [12, 25, 38, 51]:
                self._deck[value] = card.Card('King', suit)
            else:
                self._deck[value] = card.Card(str(((value % 52) - splitter) + 1), suit)
        self._reverse_lookup_deck = self.set_reverse_lookup_deck()

    def get_deck(self):
        return self._deck

    def shuffle_deck(self):
        return random.shuffle(self._random_state)

    def get_shuffled_values(self):
        return self._random_state

    def serve_card(self, the_player):
        if not isinstance(the_player, player.Player):
            raise ValueError('A card can only be served to a Player')
        deck = self.get_deck()
        state = self.get_shuffled_values()
        card_to_serve = state[0]
        state.pop()  # Remove the Card
        the_card = deck[card_to_serve]
        del deck[card_to_serve]
        the_player.add_card_to_hand(the_card)

    def explicit_serve_card(self, card_index, the_player):
        if not isinstance(card_index, int):
            raise ValueError('Card to serve must be an index in the deck')
        if not isinstance(the_player, player.Player):
            raise ValueError('A card can only be served to a Player')
        deck = self.get_deck()
        the_player.add_card_to_hand(deck[card_index])

    def explicit_serve_cards(self, cards_to_serve, the_player):
        if not isinstance(cards_to_serve, list):
            raise ValueError('Cards to serve must be a list')
        if len(cards_to_serve) != 3:
            raise ValueError('In a 3 Patti game, every hand must consist of 3 cards')
        if not isinstance(the_player, player.Player):
            raise ValueError('A card can only be served to a Player')
        [self.explicit_serve_card(item, the_player) for item in cards_to_serve]

    def add_card_to_deck(self, card_to_add):
        if isinstance(card_to_add, list):
            [self.add_card_to_deck(the_card) for the_card in card_to_add]
        if not isinstance(card_to_add, card.Card):
            raise ValueError('Only a card can be added to a deck')
        deck = self.get_deck()
        deck[int(card_to_add.get_value())] = card_to_add.get_card()

    def get_reverse_lookup_deck(self):
        return self._reverse_lookup_deck

    def set_reverse_lookup_deck(self):
        return dict([(value, key) for key, value in self.get_deck().items()])
