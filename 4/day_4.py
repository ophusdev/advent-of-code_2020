import os
import re


class DayFour():

    mandatory_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]

    optional_fields = [
        'cid'
    ]

    def check_height(height):
        if not any(unit in height for unit in ["cm", "in"]):
            return False
        return (
            150 <= int(height[:-2]) <= 193
            if "cm" in height
            else 59 <= int(height[:-2]) <= 76
        )

    fields_rules = {
        "byr": lambda k: 1920 <= int(k) <= 2002,
        "iyr": lambda k: 2010 <= int(k) <= 2020,
        "eyr": lambda k: 2020 <= int(k) <= 2030,
        "hgt": check_height,
        "hcl": lambda k: re.match('^#[a-f\d]{6}$', k) is not None,
        "ecl": lambda k: k in ["amb", "blu", "brn", "gry",
                               "grn", "hzl", "oth"],
        "pid": lambda k: len(k) == 9,
    }

    def check_height(height: str) -> bool:
        if not any(unit in height for unit in ["cm", "in"]):
            return False
        return (
            150 <= int(height[:-2]) <= 193
            if "cm" in height
            else 59 <= int(height[:-2]) <= 76
        )

    valid_passports = 0
    valid_passports_two = 0

    def __init__(self):
        self.lines = []
        self.read_list()

    def read_list(self):
        with open('./_data/data_4.txt') as f:
            contents = f.read()
            self.lines = contents.split(os.linesep + os.linesep)

    def is_valid_passport(self, passport):
        return all(field in passport for field in self.fields_rules)

    def is_valid_password_fields(self, passport):
        if self.is_valid_passport(passport):
            passport = dict(part.split(':') for part in passport.split(' '))
            return all(self.fields_rules[field](passport[field])
                       for field in self.fields_rules)

    def part_one(self):
        for passport in self.lines:
            passport = passport.replace('\n', ' ')
            if self.is_valid_passport(passport):
                self.valid_passports += 1

        return self.valid_passports

    def part_two(self):
        for passport in self.lines:
            passport = passport.replace('\n', ' ')
            if self.is_valid_password_fields(passport):
                self.valid_passports_two += 1

        return self.valid_passports_two


day_four = DayFour()
print("Number of valid password: ")
print(day_four.part_one())
print("======================================")

print("Number of valid password part two: ")
print(day_four.part_two())
