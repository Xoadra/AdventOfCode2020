# 
# 
# 
# Day 4
# Link: https://adventofcode.com/2020/day/4
# 
# 
# 

import re


def import_figures(path):
    figures, entry = [], {}
    with open(path) as file:
        for line in file.readlines():
            if line.isspace():
                figures.append(entry)
                entry = {}
            else:
                pairs = re.findall(r"[\w|#]+", line)
                for index in range(1, len(pairs), 2):
                    entry[pairs[index - 1]] = pairs[index]
        figures.append(entry)
    return figures

def valid_passports_1(passports, required):
    certified = 0
    for passport in passports:
        if all([key in passport for key in required]):
            certified += 1
        """
        if len(passport) >= 7:
            if len(passport) == 8 or "cid" not in passport:
                certified += 1
        """
    return certified

def correct_fields(passport):
    validations = 0
    for field, value in passport.items():
        if field == "byr" and "1920" <= value <= "2002":
            validations += 1
        if field == "iyr" and "2010" <= value <= "2020":
            validations += 1
        if field == "eyr" and "2020" <= value <= "2030":
            validations += 1
        if field == "hgt":
            if value[-2:] == "cm" and "150" <= value[:-2] <= "193":
                validations += 1
            elif value[-2:] == "in" and "59" <= value[:-2] <= "76":
                validations += 1
        if field == "hcl" and re.match(r"^#[0-9a-f]{6}$", value):
            validations += 1
        if field == "ecl" and re.match(r"(amb|blu|brn|gry|grn|hzl|oth)", value):
            validations += 1
        if field == "pid" and value.isdigit() and len(value) == 9:
            validations += 1
    return validations

def valid_passports_2(passports, required):
    certified = 0
    for passport in passports:
        if all([key in passport for key in required]):
            if correct_fields(passport) == 7:
                certified += 1
    return certified


figures = import_figures("input.txt")
required = "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"

result_1 = valid_passports_1(figures, required) # 228
result_2 = valid_passports_2(figures, required) # 175

print(result_1, result_2)



