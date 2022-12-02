# Day 1

import os

def cal_groups(input_dir: str) -> list:
    inventory = list()
    input_file = os.path.join(input_dir, 'day01.txt')
    with open(input_file, 'r', encoding='utf-8') as cal_input:
        cals = 0
        for line in cal_input:
            cal_int = line.strip()
            if cal_int.isdecimal():
                cals = cals + int(cal_int)
            else:
                inventory.append(cals)
                cals = 0
        inventory.append(cals)
    return inventory

## Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
print('Part 1')
for x in ['sample', 'input']:
    print(x)
    groups = cal_groups(x)
    print(max(groups))

## Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
print('Part 2')
for x in ['sample', 'input']:
    print(x)
    groups = cal_groups(x)
    groups_sorted = sorted(groups, reverse=True)
    top_three = groups_sorted[0:3]
    print(sum(top_three))
