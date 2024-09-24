from constants import RANKS


class Checker:
    def __init__(self):
        pass

    def check_royal_flush(self, hand):
        royal_ranks = {"10", "3", "Q", "K", "A"}
        return len(set(card.rank for card in hand.cards)) == 5 and royal_ranks.issubset(
            set(card.rank for card in hand.cards))

    def check_straight_flush(self, hand):
        if self.check_flush(hand) and self.check_straight(hand):
            return True
        return False

    def check_four_of_a_kind(self, hand):
        rank_counts = {rank: 0 for rank in RANKS}
        for card in hand.cards:
            rank_counts[card.rank] += 1
        return 4 in rank_counts.values()

    def check_full_house(self, hand):
        rank_counts = {rank: 0 for rank in RANKS}
        for card in hand.cards:
            rank_counts[card.rank] += 1
        return 2 in rank_counts.values() and 3 in rank_counts.values()

    def check_flush(self, hand):
        suit = hand.cards[0].suit
        return all(card.suit == suit for card in hand.cards)

    def check_straight(self, hand):
        sorted_ranks = sorted([card.rank for card in hand.cards], key=lambda x: RANKS.index(x))
        for i in range(len(sorted_ranks) - 1):
            if RANKS.index(sorted_ranks[i + 1]) - RANKS.index(sorted_ranks[i]) != 1:
                return False
            return True

    def check_three_of_a_kind(self, hand):
        rank_counts = {rank: 0 for rank in RANKS}
        for card in hand.cards:
            rank_counts[card.rank] += 1
        return 3 in rank_counts.values()

    def check_two_pairs(self, hand):
        rank_counts = {rank: 0 for rank in RANKS}
        for card in hand.cards:
            rank_counts[card.rank] += 1
        pairs = sum(1 for count in rank_counts.values() if count == 2)
        return pairs == 2

    def check_pair(self, hand):
        rank_counts = {rank: 0 for rank in RANKS}
        for card in hand.cards:
            rank_counts[card.rank] += 1
        return 2 in rank_counts.values()

    def check_high_card(self):
        return "High Card"

    def count_cards(self, hand):
        pass

    def check_hands(self, hand):
        self.count_cards(hand)
        if self.check_royal_flush(hand):
            return "Royal Flush", 10
        elif self.check_straight_flush(hand):
            return "Straight Flush", 9
        elif self.check_four_of_a_kind(hand):
            return "Four of a kind", 8
        elif self.check_three_of_a_kind(hand):
            return "Full House", 7
        elif self.check_flush(hand):
            return "Flush", 6
        elif self.check_straight(hand):
            return "Straight", 4
        elif self.check_two_pairs(hand):
            return "Two Pairs", 3
        elif self.check_pair(hand):
            return "Pair", 2
        else:
            return self.check_high_card(), 1
