
class DayThree():

    def __init__(self):
        self.lines = []
        self.read_list()

    def read_list(self):
        with open('./_data/data_3.txt') as f:
            for line in f:
                self.lines.append(list(line.strip('\n')))

    def part_one(self, right, down):
        tree_number = 0
        height, width = len(self.lines), len(self.lines[0])
        for i, row in enumerate(range(0, height, down)):
            col = (right*i) % width
            if self.lines[row][col] == '#':
                tree_number += 1

        return tree_number

    def part_two(self, path_to_check):
        # call again part_one but I van bypass this
        product = 1
        for right, down in path_to_check:
            product *= self.part_one(right, down)

        return product


day_three = DayThree()
print("Number of tree: ")
print(day_three.part_one(3, 1))
print("======================================")

path_to_check = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print("Number of tree multiplied: ")
print(day_three.part_two(path_to_check))
