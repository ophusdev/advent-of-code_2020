import time
import os
import re


def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' + "{:2.5f}"
              .format(time.time()-t) + ' sec')
        return ret
    return wrapper_method


class DayNineteen():

    def __init__(self):
        self.lines = []
        self.read_list()

    def read_list(self):
        with open('./_data/data_19.txt') as f:
            contents = f.read().split(os.linesep)
            self.lines = contents
    
    def evaluate_rules(self, rules, index):
        rule = rules[index]
        if rule[0] == 0:
            return [rule[1]]
        else:
            result = []
            for group in rule[1]:
                indices = [int(x) for x in group.split()]
                res = self.evaluate_rules(rules, indices[0])
                for i in indices[1:]:
                    parts = self.evaluate_rules(rules, i)
                    res  = [r + p for r in res for p in parts]
                result = result + res    
            return result
        return None

    @profiler
    def part_one(self):

        rules = {}
        subs  = {}
        for i, line in enumerate(self.lines):
            if len(line.strip()) == 0: 
                break
            r = line.split(':')  
            if len(r[1]) == 4:
                rules[int(r[0])] = [0, r[1][2]]
            else:
                rules[int(r[0])] = [1, r[1].split('|')]
        
        message = self.lines[i+1:]

        message_calc = self.evaluate_rules(rules, 0)
        print("sum")
        return sum([1 for message in message_calc if message in message_calc])


    def part_two(self):
        pass


day_nineteen = DayNineteen()
print("How many messages completely match rule 0??")
print(day_nineteen.part_one())
print("=========================================")
print("")
print(day_nineteen.part_two())
