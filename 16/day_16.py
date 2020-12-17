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


class DaySixteen():

    def __init__(self):
        self.lines = []
        self.read_list()
        self.extract_rules()

    def read_list(self):
        with open('./_data/data_16.txt') as f:
            contents = f.read().split(os.linesep + os.linesep)
            self.lines = contents
            self.rules = {}

    def extract_rules(self):

        #try to extract all patterns with regex
        regex_rules = re.compile(r"([a-z ]*): (\d*)-(\d*) or (\d*)-(\d*)")
        analyze_rule = self.lines[0].split('\n')

        for line in analyze_rule:
            rule, one, two, three, four = regex_rules.match(line).groups()
            ranges=set()
            for x in range (int(one),int(two)+1): ranges.add(x)
            for x in range (int(three),int(four)+1): ranges.add(x)
            self.rules[rule]=ranges

    def check_ticket(self):

        invalid_ticket = 0
        self.lines[2]  =self.lines[2].replace('nearby tickets:\n', '')
        sum_ticket = 0
        
        for ticket in self.lines[2].split('\n'):
            
            for number in ticket.split(','):
                found=True
                
                for values in self.rules.values():
                    if int(number) in values: 
                        found=False

                if found:
                    sum_ticket += int(number)
    
        return sum_ticket
 
    @profiler
    def part_one(self):
        return self.check_ticket()

    def part_two(self):
        pass



day_sixteen = DaySixteen()
print("What is your ticket scanning error rate?")
print(day_sixteen.part_one())
print("=========================================")
print("What do you get if you multiply\
    those six values together?")
print(day_sixteen.part_two())

