import time
import copy
import os
import itertools


def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' + "{:2.5f}"
              .format(time.time()-t) + ' sec')
        return ret
    return wrapper_method


class DaySeventeen():

    def __init__(self):
        self.lines = []
        self.read_list()
        self.active = '#'
        self.inactive = '.'

    def read_list(self):
        with open('./_data/data_17.txt') as f:
            contents = f.read().split(os.linesep)
            self.lines = contents

    @profiler
    def part_one(self, max_columns=24, n_cycle=6):
        grid = [[['.' for _ in range(max_columns)]
                for _ in range(max_columns)] for _ in range(max_columns)]

        for row, i in enumerate(self.lines):
            for column, j in enumerate(i):
                grid[12][row+9][column+9] = j

        for _ in range(n_cycle):
            tmp = copy.deepcopy(grid)

            for i in range(max_columns):
                for j in range(max_columns):
                    for x in range(max_columns):
                        counter = 0
                        for z in itertools.product([0, 1, -1], repeat=3):
                            if not(z == (0, 0, 0))\
                                    and (0 <= i + z[0] <= (max_columns-1)) \
                                    and (0 <= j + z[1] <= (max_columns-1)) \
                                    and (0 <= x + z[2] <= (max_columns-1)) \
                                    and grid[i+z[0]][j+z[1]][x+z[2]] == self.active:
                                counter += 1
                        if (grid[i][j][x] == self.active) and (not(2 <= counter <= 3)):
                            tmp[i][j][x] = self.inactive

                        if (grid[i][j][x] == self.inactive) and (counter == 3):
                            tmp[i][j][x] = self.active

            grid = tmp

        # Count active cubes
        count_active = 0
        for i in range(max_columns):
            for j in range(max_columns):
                for k in range(max_columns):
                    if grid[i][j][k] == self.active:
                        count_active += 1
        return count_active

    def part_two(self, max_columns=24, n_cycle=6):
        grid = [[[['.' for _ in range(max_columns)] for _ in range(max_columns)] for _ in range(max_columns)] for _ in range(max_columns)]

        for row, i in enumerate(self.lines):
            for column, j in enumerate(i):
                grid[12][12][row+9][column+9] = j

        for _ in range(n_cycle):
            tmp = copy.deepcopy(grid)

            for i in range(max_columns):
                for j in range(max_columns):
                    for x in range(max_columns):
                        for w in range(max_columns):
                            counter = 0
                            for z in itertools.product([0, 1, -1], repeat=4):
                                if not(z == (0, 0, 0, 0))\
                                        and (0 <= i + z[0] <= (max_columns-1)) \
                                        and (0 <= j + z[1] <= (max_columns-1)) \
                                        and (0 <= x + z[2] <= (max_columns-1)) \
                                        and (0 <= w + z[3] <= (max_columns-1)) \
                                        and (grid[i+z[0]][j+z[1]][x+z[2]][w+z[3]] == self.active):
                                    counter += 1

                            if (grid[i][j][x][w] == self.active) and (not(2 <= counter <= 3)):
                                tmp[i][j][x][w] = self.inactive

                            if (grid[i][j][x][w] == self.inactive) and (counter == 3):
                                tmp[i][j][x][w] = self.active

            grid = tmp

        # Count active cubes
        count_active = 0
        for i in range(max_columns):
            for j in range(max_columns):
                for k in range(max_columns):
                    for w in range(max_columns):
                        if grid[i][j][k][w] == self.active:
                            count_active += 1
        return count_active


day_seventeen = DaySeventeen()
print("How many cubes are left in the active state after the sixth cycle?")
print(day_seventeen.part_one())
print("=========================================")
print("How many cubes are left in the active state after the sixth cycle?")
print(day_seventeen.part_two())
