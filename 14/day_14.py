import os
import time


def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' + "{:2.5f}"
              .format(time.time()-t) + ' sec')
        return ret
    return wrapper_method


class DayFourthheen():

    def __init__(self):
        self.lines = []
        self.read_list()

    def read_list(self):
        with open('./_data/data_14.txt') as f:
            contents = f.read().split(os.linesep)
            self.lines = [line for line in contents]

    def apply_bitmask(self, mask, num):
        bits = [char for char in format(num, '036b')]
        for i in range(36):
            if mask[i] != 'X':
                bits[i] = mask[i]
        return int(''.join(bits), 2)

    @profiler
    def part_one(self):
        mem, mask = dict(), None

        for line in self.lines:
            line_split = line.split("=")
            if line_split[0].strip() == 'mask':
                mask = line_split[1].strip()
            else:
                number = line_split[1].strip()
                mem[line_split[0]] = self.apply_bitmask(mask, int(number))

        return sum(mem.values())

    def possibile_address(self, mask, target):
        bits = format(target, '036b')
        nums = [0]

        for i in range(36):
            pow2 = 35 - i
            if mask[i] == '0':
                if bits[i] == '1':
                    vals = [1]
                else:
                    continue
            elif mask[i] == '1':
                vals = [1]
            else:
                vals = [0, 1]
            nums = [
                num + val * 2**pow2
                for num in nums
                for val in vals
            ]
        return nums

    @profiler
    def part_two(self):
        mem, mask = dict(), None

        for line in self.lines:
            line_split = line.split("=")
            if line_split[0].strip() == 'mask':
                mask = line_split[1].strip()
            else:
                number = int(line_split[1].strip())
                location_address = line_split[0].strip()
                location_address = int(location_address.replace('mem', '')
                                       .replace('[', '').replace(']', ''))

                possibile_address = self.possibile_address(mask, location_address)
                for address in possibile_address:
                    mem[address] = number

        return sum(mem.values())


day_fourthteen = DayFourthheen()
print("What is the sum of all values left in memory after it completes?")
print(day_fourthteen.part_one())
print("=========================================")
print("What is the sum of all values left in memory after it completes?")
print(day_fourthteen.part_two())
