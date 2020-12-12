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


class DayTwelve():

    def __init__(self):
        self.lines = []
        self.read_list()
        self.instruction = {'N': (0, 1), 'S': (0, -1),
                            'W': (1, 0), 'E': (-1, 0)}
        self.rotation = {'R': (-1, 1), 'L': (1, -1)}

    def read_list(self):
        self.operations = []
        with open('./_data/data_12.txt') as f:
            contents = f.read().split(os.linesep)
            self.lines = [line for line in contents]

    def move(self, action, value, x, y, wx, wy):
        if action in self.instruction:
            x += self.instruction[action][0] * value
            y += self.instruction[action][1] * value

        if action in self.rotation:
            for i in range(value // 90):
                wx, wy = wy * self.rotation[action][0], wx * self.rotation[action][1]

        if action == 'F':
            x += wx * value
            y += wy * value

        return x, y, wx, wy

    def move_waypoints(self, action, value, x, y, wx, wy):

        if action in self.instruction:
            wx += self.instruction[action][0] * value
            wy += self.instruction[action][1] * value

        if action in self.rotation:
            for i in range(value // 90):
                wx, wy = wy * self.rotation[action][0], wx * self.rotation[action][1]

        if action == 'F':
            x += wx * value
            y += wy * value

        return x, y, wx, wy

    @profiler
    def part_one(self):
        actions = [{'action': 'E', 'value': 0}]

        for line in self.lines:
            actions.append({'action': line[0:1], 'value': int(line[1:])})

        x, y = 0, 0
        wx, wy = -1, 0
        for action in actions:
            x, y, wx, wy = self.move(action['action'], action['value'], x, y, wx, wy)

        return abs(x) + abs(y)

    @profiler
    def part_two(self):

        actions = []
        for line in self.lines:
            actions.append({'action': line[0:1], 'value': int(line[1:])})

        x, y = 0, 0
        wx, wy = -10, 1  # start in 10E, 1N
        for action in actions:
            x, y, wx, wy = self.move_waypoints(action['action'], action['value'], x, y, wx, wy)

        return abs(x) + abs(y)


day_twelve = DayTwelve()
print("What is the Manhattan distance between\
      that location and the ship's starting position?")
print(day_twelve.part_one())
print("=========================================")
print("What is the Manhattan distance between\
      that location and the ship's starting position?")
print(day_twelve.part_two())
