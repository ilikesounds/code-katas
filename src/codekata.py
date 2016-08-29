class Card(object):

    def _repr__(self):
        return repr(str(self.card_val))

    def assign_rank(self, val):
        if val == 'A':
            return 0
        elif val == '2':
            return 1
        elif val == '3':
            return 2
        elif val == '4':
            return 3
        elif val == '5':
            return 4
        elif val == '6':
            return 5
        elif val == '7':
            return 6
        elif val == '8':
            return 7
        elif val == '9':
            return 8
        elif val == 'T':
            return 9
        elif val == 'J':
            return 10
        elif val == 'Q':
            return 11
        elif val == 'K':
            return 12

    def __init__(self, val):
        self.card_val = val
        self.card_rank = assign_rank(val)


def sort_cards(deck):

    sorted_deck = []

    for card in deck:
        sorted_deck.append(Card(card))
        sorted_deck = sorted(sorted_deck, key=lambda card: card.card_rank)
        return [x.card_val for x in sorted_deck]
