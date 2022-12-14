from itertools import groupby

from params import LOCAL_DATA_PATH

data_path = LOCAL_DATA_PATH + '/Day1_data.txt'

with open(data_path) as f:

    data = f.readlines()

def part1(data):

    '''Return the highest total calories carried by an elf'''

    data_clean = [data.replace('\n','') for data in data]
    elves_split = [list(sub) for ele, sub in groupby(data_clean, key = bool) if ele]
    elves_split_numeric = [[int(numerics) for numerics in strings] for strings in elves_split]
    elf_cal_sum = [sum(elf) for elf in elves_split_numeric]

    max_value = max(elf_cal_sum)
    max_index = elf_cal_sum.index(max_value)

    output = f"Elf no. {max_index+1} had the most calories, with {max_value}"

    return output

def part2(data):

    '''Return the sum of calories for the three elves with the most'''

    # Same as part1
    data_clean = [data.replace('\n','') for data in data]
    elves_split = [list(sub) for ele, sub in groupby(data_clean, key = bool) if ele]
    elves_split_numeric = [[int(numerics) for numerics in strings] for strings in elves_split]
    elf_cal_sum = [sum(elf) for elf in elves_split_numeric]

    # New code

    index_values = [(i,x) for x,i in enumerate(elf_cal_sum)]
    top_three_elves = sorted(index_values, reverse=True)[0:3]

    elf_dict = {}

    for elf_cal, elf_id in top_three_elves:
        elf_dict[elf_id] = elf_cal

    top_three_ids = list(elf_dict.keys())
    total_cals = sum(elf_dict.values())

    output = f"The top three elves are {top_three_ids}!\nThey collectively have {total_cals} calories"

    return output

if __name__ == '__main__':

    part_1 = part1(data)
    part_2 = part2(data)

    print(f'Part 1:\n{part_1}\n\nPart 2:\n{part_2}')
