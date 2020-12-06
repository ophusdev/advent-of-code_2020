import os


class DaySix():

    def __init__(self):
        self.lines = []
        self.read_list()

    def read_list(self):
        with open('./_data/data_6.txt') as f:
            contents = f.read().split(os.linesep + os.linesep)
            self.lines = [line for line in contents]

    def count(self, line):
        return len(list(set(line)))
    
    def part_one(self):
        counter = [self.count(line.replace('\n','') ) for line in self.lines]
        return sum(counter)

    def count_all_yes(self, line):
        return len(list(set(line)))

    def part_two(self):
        people = [[set(p) for p in data.split()] for data in self.lines]
        intersect_people = [p[0].intersection(*p) for p in people]

        return sum(len(p) for p in intersect_people)

day_six = DaySix()
print("What is the sum of those counts?")
print(day_six.part_one())
print("======================================")

print(day_six.part_two())