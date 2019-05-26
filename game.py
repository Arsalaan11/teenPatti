from Assignment1 import deck
from Assignment1 import player
import traceback
import sys


def minelements(seq):
    m = min(seq)
    return [i for i, j in enumerate(seq) if j == m]


if __name__ == '__main__':
    try:
        print('Please Enter the sequence of cards for each player, '
              'for example [[ 12, 23, 45 ], [ 0, 32, 50 ], [ 25, 6, 17 ], [ 22, 33, 44 ], [ 43, 49, 16 ]]')
        if sys.version_info[0] >= 3:
            input_of_players_and_cards = eval(input())
        else:
            input_of_players_and_cards = input()
        the_deck = deck.Deck()
        number_of_players = len(input_of_players_and_cards)
        print('Gathering Players...')
        players = [player.Player(index) for index in range(number_of_players)]
        print('Distributing cards...')
        [the_deck.explicit_serve_cards(the_hand, players[index]) for index, the_hand in enumerate(input_of_players_and_cards)]
        print('Calculating Ranks...')
        ranks_of_players = [the_player.calculate_rank(the_deck).get_rank() for the_player in players]
        winner = minelements(ranks_of_players)
        if len(winner) > 1:
            print('The match is a tie. The winners are {}'.format(winner))
        else:
            print('The winner is {}'.format(winner))

    except Exception as e:
        print(e)
        print(traceback.print_exc())
