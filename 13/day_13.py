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


class DayThirtheen():

    def __init__(self):
        self.lines = []
        self.read_list()

    def read_list(self):
        with open('./_data/data_13.txt') as f:
            contents = f.read().split(os.linesep)
            self.lines = [line for line in contents]

    @profiler
    def part_one(self):
        timestamp = int(self.lines[0])
        bus_list = self.lines[1].split(',')

        bus_time = {}
        for bus in bus_list:
            if bus != 'x':
                bus_time[int(bus)] = (timestamp - (timestamp % int(bus)) + int(bus))

        next_bustime = min([b for b in bus_time.values()])
        next_bus = [key for key, bus in bus_time.items() if bus == next_bustime][0]
        return ((next_bustime - timestamp)*next_bus)

    # This function checks through values based on the cumulative product of buses and previously returned value
    def calculord(self, bus, cum_product, offset, timeoffset):
        i = 1
        check = False
        while check is not False:
            value = i * cum_product + offset - timeoffset
            if value % bus == 0:
                return value, bus*cum_product
                check = True
            i += 1

    @profiler
    def part_two(self):

        bus_time = self.lines[1].split(',')

        bus_list = [int(i) for i in bus_time if i != 'x']

        count_missing_x = 0
        time_list = []
        for bus in bus_time[1:]:
            if bus == 'x':
                count_missing_x += 1
            else:
                time_list.append(count_missing_x + 1)
                count_missing_x = 0
        time_list.append(1)

        # Loop through the list backwards, using each pass to reduce the set of values that need to be checked
        offset = 0
        cum_product = 1
        for i in range(len(bus_list)-1, -1, -1):
            bus = bus_list[i]
            timeoffset = time_list[i]
            offset, cum_product = self.calculord(bus, cum_product, offset, timeoffset)

        return offset


day_thirteen = DayThirtheen()
print("What is the ID of the earliest bus you can take to the\
    airport multiplied by the number of minutes you'll need to wait for that bus?")
print(day_thirteen.part_one())
print("=========================================")
print("What is the earliest timestamp such that all of the\
    listed bus IDs depart at offsets matching their positions in the list?")
print(day_thirteen.part_two())
