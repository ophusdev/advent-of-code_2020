import time
import os


def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' + "{:2.5f}"
              .format(time.time()-t) + ' sec')
        return ret
    return wrapper_method


class DayTwentyTwo():

    def __init__(self):
        self.lines = []
        self.player_one = []
        self.player_two = []
        self.read_list()

    def read_list(self):
        with open('./_data/data_22.txt') as f:
            contents = f.read().split(os.linesep + os.linesep)
            self.lines = contents

        for i, line in enumerate(self.lines):
            deck_line = line.split(':')[1]

            if i == 0:
                for card in deck_line.split('\n'):
                    if card != '':
                        self.player_one.append(int(card))
                    # [self.player_one.append(card) for card in deck_line.split('\n')]
            else:
                for card in deck_line.split('\n'):
                    if card != '':
                        self.player_two.append(int(card))
                    # [self.player_two.append(card) for card in deck_line.split('\n')]

    @profiler
    def part_one(self):

        round_n = 1
        total_points = 0
        while True:

            if len(self.player_one) == 0 or len(self.player_two) == 0:
                break

            print(f"--- {round_n} ---")
            print(f"Player 1: {self.player_one}")
            print(f"Player 2: {self.player_two}")

            card_one = self.player_one.pop(0)
            card_two = self.player_two.pop(0)

            print(f"{card_one} vs {card_two}")

            if card_one > card_two:
                self.player_one.append(card_one)
                self.player_one.append(card_two)
            else:
                self.player_two.append(card_two)
                self.player_two.append(card_one)

            round_n = round_n + 1

        total_points = self.player_one + self.player_two
        return sum((c * (len(total_points) - i) for i, c in enumerate(total_points)))

    def recursive_game(self, game, p1, p2):
        seen = set()
        game[0] += 1
        this_game = game[0]
        decks = (tuple(p1), tuple(p2))
        while p1 and p2:
            if decks in seen:
                return 1
            seen.add(decks)
            c1 = p1.pop(0)
            c2 = p2.pop(0)
            if len(p1) >= c1 and len(p2) >= c2:
                winner = self.recursive_game(game, p1[:c1], p2[:c2])
            else:
                if c1 > c2:
                    winner = 1
                else:
                    winner = 2
            if winner == 1:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
            decks = (tuple(p1), tuple(p2))

        if this_game == 1:
            return p1, p2
        else:
            return 1 if p1 else 2

    def part_two(self):

        deck_one, deck_two = self.recursive_game([0], self.player_one, self.player_two)
        return sum((c * (len(deck_one) - i) for i, c in enumerate(deck_one)))


day_twentytwo = DayTwentyTwo()
print("What is the winning player's score?")
print(day_twentytwo.part_one())
day_twentytwo = DayTwentyTwo()
print("=========================================")
print("What is the winning player's score?")
print(day_twentytwo.part_two())
