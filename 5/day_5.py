import math


class DayFive():

    def __init__(self):
        self.lines = []
        self.read_list()

    def read_list(self):
        with open('./_data/data_5.txt') as f:
            for line in f:
                self.lines.append(list(line.strip('\n')))

    def calculate_seat(self, code):
        min_range, max_range = 0, 127
        min_columns, max_columns = 0, 8
        
        all_digits = [digit for digit in code]

        for digit in all_digits[:7]:
            if digit == 'F':
                gap = math.floor((max_range + min_range) / 2)
                max_range = gap
            
            if digit == 'B':
                gap = math.ceil((max_range + min_range) / 2)
                min_range = gap
    
        for digit in all_digits[7:]:
            if digit == 'L':
                gap = math.floor((max_columns + min_columns) / 2)
                max_columns = gap
            
            if digit == 'R':
                gap = math.ceil((max_columns + min_columns) / 2)
                min_columns = gap

        return min_range * 8 + min_columns
    
    def part_one(self):
        all_results = []

        for seat in self.lines:
            all_results.append(self.calculate_seat(seat))

        sorted_numbers = sorted(all_results)
        return sorted_numbers[len(sorted_numbers)-1]
    
    def part_two(self):
        all_boardingpass = []

        for seat in self.lines:
            all_boardingpass.append(self.calculate_seat(seat))

        sorted_numbers = sorted(all_boardingpass)

        all_seats = []

        for i in range(sorted_numbers[0], sorted_numbers[len(sorted_numbers)-1]):
            all_seats.append(i)

        return (list(set(all_seats) - set(sorted_numbers)))


day_five = DayFive()
print("Number of seats: ")
print(day_five.part_one())
print("======================================")

print("Your seat is: ")
print(day_five.part_two()[0])