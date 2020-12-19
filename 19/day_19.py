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
            contents = f.read().split('\n')
            self.lines = contents

    def calc_rules(self, rules, index):
        rule = rules[index]
        if rule[0] == 0:
            return [rule[1]]
        else:
            result = []
            for group in rule[1]:
                indices = [int(x) for x in group.split()]
                res = self.calc_rules(rules, indices[0])
                for i in indices[1:]:
                    parts = self.calc_rules(rules, i)
                    res  = [r + p for r in res for p in parts]
                result = result + res    
            return result
        return None
    
    def start_one(self, rules, message):
        result = self.calc_rules(rules, 0)
        return sum([1 for m in message if m in result])

    @profiler
    def part_one(self):
        rules  = {}

        for index, line in enumerate(self.lines):
            if len(line.strip()) == 0: 
                break
            rule = line.split(':')  
            if len(rule[1]) == 4:
                rules[int(rule[0])] = [0, rule[1][2]]
            else:
                rules[int(rule[0])] = [1, rule[1].split('|')]
        
        message = self.lines[index+1:]

        return self.start_one(rules, message)


    def part_two(self):
        rules  = {}

        for index, line in enumerate(self.lines):
            if len(line.strip()) == 0: 
                break
            rule = line.split(':')  
            if len(rule[1]) == 4:
                rules[int(rule[0])] = [0, rule[1][2]]
            else:
                rules[int(rule[0])] = [1, rule[1].split('|')]
        
        message = self.lines[index+1:]

        rules[8] = [1, ['42', '42 8']]
        rules[11] = [1, ['42 31', '42 11 31']]
        return None


day_nineteen = DayNineteen()
print("How many messages completely match rule 0?")
print(day_nineteen.part_one())
print("=========================================")
print("After updating rules 8 and 11, how many messages completely match rule 0?")
print(day_nineteen.part_two())
