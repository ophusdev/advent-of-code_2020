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


class DayEighteen():

    def __init__(self):
        self.lines = []
        self.read_list()

    def read_list(self):
        with open('./_data/data_18.txt') as f:
            contents = f.read().split(os.linesep)
            self.lines = contents

    def extract_digit(self, line):
        characters = []
        symbols =  re.findall(r"[\d]+|[+*\(\)]", line)
        
        while len(symbols) > 0:
            digit = symbols.pop(0)

            if digit.isdigit():
                characters.append(int(digit))
            elif digit in ['+', '*']:
                characters.append(digit)
            elif digit  == '(':
                level = 1
                nested = ''
                while True:
                    digit = symbols.pop(0)
                    if digit in ["(", ")"]:
                        level = level + ")x(".index(digit) - 1
                        if level <= 0:
                            break
                    nested += digit + " "

                characters.append(self.extract_digit(nested))
    
        result = 0
        op = "+"
        while len(characters) > 0:
            token = characters.pop(0)
            if type(token) is int:
                if op == "+":
                    result += token
                else:
                    result *= token
            elif token in ["+", "*"]:
                op = token
        
        return result

    def calc_precedence(self, line):
        characters = []
        symbols =  re.findall(r"[\d]+|[+*\(\)]", line)
        
        while len(symbols) > 0:
            digit = symbols.pop(0)

            if digit.isdigit():
                characters.append(int(digit))
            elif digit in ['+', '*']:
                characters.append(digit)
            elif digit  == '(':
                level = 1
                nested = ''
                while True:
                    digit = symbols.pop(0)
                    if digit in ["(", ")"]:
                        level = level + ")x(".index(digit) - 1
                        if level <= 0:
                            break
                    nested += digit + " "

                characters.append(self.calc_precedence(nested))

         #need to reorder operations
        if "+" in characters and "*" in characters:
            characters_ordered = []
            while len(characters) > 0:
                token = characters.pop(0)
                if token == "+":
                    characters_ordered.insert(len(characters_ordered) - 1, "(")
                    characters_ordered.append("+")
                    characters_ordered.append(characters.pop(0))
                    characters_ordered.append(")")
                else:
                    characters_ordered.append(token)

            return self.calc_precedence(" ".join(str(t) for t in characters_ordered))
        
        result = 0
        op = "+"
        while len(characters) > 0:
            token = characters.pop(0)
            if type(token) is int:
                if op == "+":
                    result += token
                else:
                    result *= token
            elif token in ["+", "*"]:
                op = token
        
        return result
    
    @profiler
    def part_one(self):
        all_sum = []
        for line in self.lines:
            result = self.extract_digit(line)
            all_sum.append(result)
        
        return sum(all_sum)

    def part_two(self):
        all_sum = []
        for line in self.lines:
            result = self.calc_precedence(line)
            all_sum.append(result)
        
        return sum(all_sum)


day_eigthteen = DayEighteen()
print("Evaluate the expression on each line of the homework;\
    what is the sum of the resulting values?")
print(day_eigthteen.part_one())
print("=========================================")
print("What do you get if you add up the results of\
    evaluating the homework problems using these new rules?")
print(day_eigthteen.part_two())
