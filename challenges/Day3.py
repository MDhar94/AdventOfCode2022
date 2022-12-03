from aocd import get_data
import string
from params import LOCAL_TOKEN_PATH

with open(LOCAL_TOKEN_PATH+'token.txt') as f:
    token = f.read().strip('\n')

data = get_data(session=token,day=3,year=2022)

def part1(data):

    data_split = data.split(sep='\n')

    rucksacks = []

    for rucksack in data_split:
        rucksack_size = int(len(rucksack)/2)
        temp_list = []
        temp_list.append(rucksack[:rucksack_size])
        temp_list.append(rucksack[rucksack_size:])
        rucksacks.append(temp_list)

    priority_scores = []

    for sack in rucksacks:
        common_value = list(set(sack[0]).intersection(sack[1]))[0]
        priority_score = string.ascii_letters.index(common_value) + 1
        priority_scores.append(priority_score)

    return sum(priority_scores)


def part2(data):

    data_split = data.split(sep='\n')

    badge_values = []

    for i in range(0,len(data_split),3):

        temp_group = []

        temp_group.append(data_split[i])
        temp_group.append(data_split[i+1])
        temp_group.append(data_split[i+2])

        badge = set(temp_group[0]) & set(temp_group[1]) & set(temp_group[2])
        badge_score = string.ascii_letters.index(list(badge)[0]) + 1
        badge_values.append(badge_score)

    return sum(badge_values)

if __name__ == '__main__':

    output_part1 = part1(data)
    output_part2 = part2(data)

    print(output_part1, output_part2)
