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


class DayEleven():

    def __init__(self):
        self.lines = []
        self.read_list()
        self.grid = []

    def read_list(self):
        self.operations = []
        with open('./_data/data_11.txt') as f:
            contents = f.read().split(os.linesep)
            self.lines = [line for line in contents]

    def build_grid(self, grid_to_validate):
        grid = grid_to_validate
        changed_grid = []
        for row in range(len(grid)):
            newrow = ''
            for col in range(len(grid[0])):
                adj = []
                for x in (-1, 0, 1):
                    for y in (-1, 0, 1):
                        if x == y == 0:
                            continue
                        if 0 <= row+x < len(grid) and 0 <= col+y < len(grid[0]):
                            adj.append(grid[row+x][col+y])

                if grid[row][col] == 'L' and '#' not in adj:
                    newrow += '#'
                elif grid[row][col] == '#' and adj.count('#') >= 4:
                    newrow += 'L'
                else:
                    newrow += grid[row][col]
            changed_grid.append(newrow)
        return changed_grid

    def build_grid_two(self, grid_to_validate):
        grid = grid_to_validate
        changed_grid = []
        for row in range(len(grid)):
            newrow = ''
            for col in range(len(grid[0])):
                adj = []
                for x in (-1, 0, 1):
                    for y in (-1, 0, 1):
                        if x == y == 0:
                            continue
                        i = 1
                        while 0 <= row+i*x < len(grid) and 0 <= col+i*y < len(grid[0]):
                            ch = grid[row+i*x][col+i*y]
                            if ch != '.':
                                adj.append(ch)
                                break
                            i += 1
                if grid[row][col] == 'L' and '#' not in adj:
                    newrow += '#'
                elif grid[row][col] == '#' and adj.count('#') >= 5:
                    newrow += 'L'
                else:
                    newrow += grid[row][col]
            changed_grid.append(newrow)
        return changed_grid

    @profiler
    def part_one(self):

        grid_to_validate = self.lines

        while True:
            changed_grid = self.build_grid(grid_to_validate)
            if grid_to_validate == changed_grid:
                return ''.join(changed_grid).count('#')

            grid_to_validate = changed_grid

    @profiler
    def part_two(self):
        grid_to_validate = self.lines

        while True:
            changed_grid = self.build_grid_two(grid_to_validate)
            if grid_to_validate == changed_grid:
                return ''.join(changed_grid).count('#')

            grid_to_validate = changed_grid


day_eleven = DayEleven()
print("What is the first number that does not have this property?")
print(day_eleven.part_one())
print("=========================================")
print("how many seats end up occupied?")
print(day_eleven.part_two())
