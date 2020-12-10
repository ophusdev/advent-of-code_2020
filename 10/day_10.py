import os
from functools import lru_cache


class DayTen():

    def __init__(self):
        self.lines = []
        self.read_list()

    def read_list(self):
        self.operations = []
        with open('./_data/data_10.txt') as f:
            contents = f.read().split(os.linesep)
            self.lines = [int(line) for line in contents]

    def part_one(self):

        self.lines.sort()
        data = self.lines
        differences_3 = 0
        differences_1 = 0

        for p, n in zip(data[:-1], data[1:]):
            if n - p == 3:
                differences_3 += 1
            elif n - p == 1:
                differences_1 += 1

        return (differences_1 + 1) * (differences_3 + 1)

    @lru_cache
    def calculate_combinations(self, position, target):
        if position == target:
            return 1
        count = 0
        for i in range(1, 4):
            if position + i not in self.lines:
                continue
            count += self.calculate_combinations(position + i, target)
        return count

    def part_two(self):
        max_number = max(self.lines)
        return self.calculate_combinations(0, max_number)


day_ten = DayTen()
print("What is the first number that does not have this property?")
print(day_ten.part_one())
print("=========================================")
print("What is the total number of distinct ways you \
        can arrange the adapters to connect the charging \
        outlet to your device?")
print(day_ten.part_two())
