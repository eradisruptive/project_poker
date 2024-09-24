from deck import Deck
from hand import Hand
from checker import Checker
from stats import Stats


class Application:
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand()
        self.checker = Checker()
        self.stats = Stats("stats.txt")

    def play(self):
        while True:
            print("\nNew Hand")
            self.deck.shuffle()
            self.hand.cards = [self.deck.deal() for _ in range(5)]
            for i, card in enumerate(self.hand.cards):
                print(f"{i+1}: {card}")
            choice = input("\nEnter the indices of the cards to replace (e.g., '1,2,3') or press Enter to keep them: ")
            if choice:
                indices_to_replace = [int(index) - 1 for index in choice.split()]
                self.hand.discard(indices_to_replace)
                self.hand.cards.extend(self.deck.deal() for _ in range(len(indices_to_replace)))
                for i, card in enumerate(self.hand.cards):
                    print(f"{i+1}: {card}")
            result, score = self.checker.check_hands(self.hand)
            print("Result: ", result)
            print("Score", score)

            if score > 1:
                self.stats.increase_stats(result)

            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                break

            show_stats = input("\nDo you want to see statistics? (yes/no): ").lower()
            if show_stats == "yes":
                self.stats.show_stats()


if __name__ == "__main__":
    app = Application()
    app.play()
