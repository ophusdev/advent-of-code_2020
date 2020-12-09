import os
from collections import deque

class DayNine():

    def __init__(self):
        self.lines = []
        self.read_list()
        self.accumulator = 0

    def read_list(self):
        self.operations = []
        with open('./_data/data_9.txt') as f:
            contents = f.read().split(os.linesep)
            self.lines = [int(line) for line in contents]
    
    def is_valid(self, number, preamble):
        found_number = set()
        
        for i in preamble:
            if number - i in found_number:
                return True
            found_number.add(i)

        return False

    def part_one(self, preamble_init=25):
        
        preamble = preamble_init
        preamble_list = self.lines[:preamble]
        list_to_analyze = self.lines[preamble:]

        for n in list_to_analyze:
            if not self.is_valid(n, preamble_list):
                return n
                break
            
            preamble_list.pop(0)
            preamble_list.append(n)
        
    def part_two(self, preamble_init=25):
        preamble = preamble_init

        target_number = self.part_one(preamble)

        contiguous_set = deque([])
        contiguous_sum = 0

        for n in self.lines:
            while contiguous_sum > target_number:
                contiguous_sum -= contiguous_set.popleft()
            
            if contiguous_sum == target_number:
                break
                
            contiguous_set.append(n)
            contiguous_sum += n

        return max(contiguous_set) + min(contiguous_set)


day_nine = DayNine()
print("What is the first number that does not have this property?")
print(day_nine.part_one())

print("======================================")
print("What is the encryption weakness in your XMAS-encrypted list of numbers?")
print(day_nine.part_two())
