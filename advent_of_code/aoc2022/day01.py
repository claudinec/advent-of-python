# Day 1

import os


def cals_groups(data_suffix: str) -> list:
    inventory = list()
    data_file = os.path.join("data", f"day01-{data_suffix}.txt")
    with open(data_file, "r", encoding="utf-8") as cals_input:
        cals_int = 0
        for line in cals_input:
            cals_str = line.strip()
            if cals_str.isdecimal():
                cals_int = cals_int + int(cals_str)
            else:
                inventory.append(cals_int)
                cals_int = 0
        inventory.append(cals_int)
    return inventory


for suffix in ["example", "input"]:
    print(suffix)
    groups = cals_groups(suffix)

    ## Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    print("Part 1")
    print(max(groups))

    ## Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
    print("Part 2")
    groups_sorted = sorted(groups, reverse=True)
    top_three = groups_sorted[:3]
    print(sum(top_three))
