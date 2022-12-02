# Day 1a

import os

## Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
def max_cals(input_dir: str) -> int:
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
    return max(inventory)

for x in ['sample', 'input']:
    print(x)
    print(max_cals(x))
