

class DayTwo():

    lines = []
    valid_password = 0
    valid_position = 0

    def __init__(self):
        self.read_list()

    def read_list(self):
        with open('./_data/data_2.txt') as f:
            self.lines = [line.rstrip() for line in f]

    def part_one(self):

        for line in self.lines:
            occurence_string = line.split(":")

            occurence_values = occurence_string[0].split(" ")

            min_value = int(occurence_values[0].split("-")[0])
            max_value = int(occurence_values[0].split("-")[1])

            char_to_find = occurence_values[1]

            string_to_evaluate = occurence_string[1].strip()

            if self.is_valid_count(string_to_evaluate, char_to_find,
                                   min_value, max_value):
                self.valid_password += 1

    def is_valid_count(self, string_to_evaluate, char_to_find,
                       min_value, max_value):

        if string_to_evaluate.count(char_to_find) >= min_value and \
           string_to_evaluate.count(char_to_find) <= max_value:
            return True

        return False

    def part_two(self):

        for line in self.lines:
            occurence_string = line.split(":")

            occurence_values = occurence_string[0].split(" ")

            position_one = int(occurence_values[0].split("-")[0])
            position_two = int(occurence_values[0].split("-")[1])

            char_to_find = occurence_values[1]

            string_to_evaluate = occurence_string[1].strip()

            if self.is_valid_position(string_to_evaluate, char_to_find,
                                      position_one, position_two):
                self.valid_position += 1

    def is_valid_position(self, string_to_evaluate, char_to_find,
                          position_one, position_two):

        only_one_occurrence = 0

        if string_to_evaluate[position_one-1] == char_to_find:
            only_one_occurrence += 1

        if string_to_evaluate[position_two-1] == char_to_find:
            only_one_occurrence += 1

        return True if only_one_occurrence == 1 else False


day_two = DayTwo()
day_two.part_one()
print("Number valid password:")
print(day_two.valid_password)
print("=======================")

print("Number valid password with new policy:")
day_two.part_two()
print(day_two.valid_position)
