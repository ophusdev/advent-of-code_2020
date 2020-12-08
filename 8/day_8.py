import os


class DayEight():

    def __init__(self):
        self.operations = []
        self.read_list()
        self.accumulator = 0

    def read_list(self):
        self.operations = []
        with open('./_data/data_8.txt') as f:
            contents = f.read().split(os.linesep)
            for line in contents:
                op, value = line.split(' ')
                value = int(value)
                self.operations.append({'op': op, 'value': value, 'executed': False})

    def part_one(self, position):

        new_position = position

        try:
            op = self.operations[position]['op']
            value = self.operations[position]['value']
        except IndexError:
            return

        if self.operations[position]['executed']:
            return self.accumulator

        if op == 'acc':
            self.accumulator += value
            new_position += 1

        if op == 'nop':
            new_position += 1

        if op == 'jmp':
            new_position += value

        self.operations[position]['executed'] = True
        return self.part_one(new_position)

    def part_two(self):
        self.read_list()

        for i in range(len(self.operations)-1):
            self.read_list()
            self.accumulator = 0
            if self.operations[i]['op'] == 'jmp':
                self.operations[i]['op'] = 'nop'

            elif self.operations[i]['op'] == 'nop':
                self.operations[i]['op'] = 'jmp'

            if self.part_one(0) is not None:
                break


day_eight = DayEight()
print("what value is in the accumulator?")
day_eight.part_one(0)
print(day_eight.accumulator)

print("======================================")
print("What is the value of the accumulator after the program terminates")
day_eight = DayEight()
day_eight.part_two()
print(day_eight.accumulator)
