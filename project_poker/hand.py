class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def discard(self, indices):
        for index in sorted(indices, reverse=True):
            self.cards.pop(index)
