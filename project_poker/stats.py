class Stats:
    def __init__(self, filename):
        self.filename = filename
        self.stats = self.load_stats()

    def load_stats(self):
        try:
            with open(self.filename, "r") as file:
                stats = {}
                for line in file:
                    key, value = line.strip().split(",")
                    stats[key] = int(value)
                return stats
        except FileNotFoundError:
            return {}

    def save_stats(self):
        with open(self.filename, "w") as file:
            for key, value in self.stats.items():
                file.write(f"{key}, {value}\n")

    def increase_stats(self, combination):
        self.stats[combination] = self.stats.get(combination, 0) + 1

    def show_stats(self):
        print("\nStatistics: ")
        print("-" * 14)
        print("|  Combination   | Count |")
        print("-" * 24)
        for combination, count in self.stats.items():
            print(f"| {combination.ljust(10)} | {str(count).rjust(5)} |")


if __name__ == "__main__":
    stats = Stats("stats.txt")
    stats.increase_stats("Royal Flush")
    stats.increase_stats("Full House")
    stats.save_stats()
    stats.show_stats()