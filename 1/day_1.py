from itertools import permutations
import math


class DayOne:

    all_data = []
    target = None
    pair_couple = []
    tuple_n = []

    def __init__(self, target):
        self.target = target
        self.read_list()

    def read_list(self):

        all_data = []
        lines = []

        with open('./_data/data_1.txt') as f:
            lines = f.readlines()

        for line in lines:
            all_data.append(int(line.strip()))

        self.all_data = all_data

    def pair_numbers(self):
        all_data = self.all_data
        for num in all_data:
            if num < self.target:
                pair = int(self.target) - int(num)
                if pair in all_data:
                    self.pair_couple = (pair, num)

    def part_one(self):
        return math.prod(self.pair_couple)

    def tuple_numbers(self):
        numbers = [pair for pair in permutations(self.all_data, 3)
                   if sum(pair) == self.target]

        if len(numbers) > 0:
            self.tuple_n = numbers[0]

    def part_two(self):
        return math.prod(self.tuple_n)


dayOne = DayOne(2020)
dayOne.pair_numbers()

print(f"Pair numbers is {dayOne.pair_couple}")
print(f"Solution one is {dayOne.part_one()}")
print("==============================")

dayOne.tuple_numbers()
print(f"Tuple numbers is {dayOne.tuple_n}")
print(f"Solution one is {dayOne.part_two()}")
print("==============================")
