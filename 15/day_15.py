import time


def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' + "{:2.5f}"
              .format(time.time()-t) + ' sec')
        return ret
    return wrapper_method


class DayFifteen():

    def __init__(self):
        self.lines = []
        self.read_list()

    def read_list(self):
        with open('./_data/data_15.txt') as f:
            contents = f.read().split(',')
            self.lines = [int(line) for line in contents]

    @profiler
    def part_one(self, target):
        spoken = {}

        for i in range(len(self.lines)):
            spoken[self.lines[i]] = i + 1

        last_number = self.lines[-1]

        for i in range(len(self.lines) + 1, target + 1):

            if last_number in spoken:
                calc_number = i - 1 - spoken[last_number]
            else:
                calc_number = 0

            spoken[last_number] = i - 1
            last_number = calc_number

        return last_number


day_fifteen = DayFifteen()
print("what will be the 2020th number spoken?")
print(day_fifteen.part_one(2020))
print("=========================================")
print("Given your starting numbers, what will\
    be the 30000000th number spoken?")
print(day_fifteen.part_one(30000000))
