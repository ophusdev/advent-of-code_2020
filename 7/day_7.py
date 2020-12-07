import os
import re


class DaySeven():

    def __init__(self):
        self.lines = []
        self.read_list()
        self.bags = set()
        self.colors = {}
        self.parse_data()

    def read_list(self):
        with open('./_data/data_7.txt') as f:
            contents = f.read().split(os.linesep)
            self.lines = [line for line in contents]

    def part_one(self, color):
        for lines in self.lines:
            if line := re.search(rf"^(.*) bags contain.*{color}", lines):
                self.bags.add(line.group(1))
                self.part_one(line.group(1))

    def parse_data(self,):
        for line in self.lines:
            color, part_two = line.split('bags contain')
            part_two = [i for i in list(map(lambda x: x.strip(),
                        re.sub(r'(\.|bag[s]?)', '', part_two).split(', ')))
                        if i != 'no other']

            expanded_part_two = []
            for content in part_two:
                # need number
                cnt = int(re.match(r'[0-9]+(?=\s\w)', content)[0])
                content = re.sub(r'^\d+', '', content).strip()
                expanded_part_two += [content] * cnt
            self.colors[color.strip()] = expanded_part_two

    def part_two(self, color):
        if len(self.colors[color]) == 0:
            return 0

        return sum(map(lambda k: self.part_two(k),
                   self.colors[color])) + len(self.colors[color])


day_seven = DaySeven()
print("How many bag colors can eventually \
      contain at least one shiny gold bag?")
day_seven.part_one("shiny gold")
print(len(day_seven.bags))
print("======================================")
print(day_seven.part_two('shiny gold'))
