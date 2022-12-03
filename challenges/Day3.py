from aocd import get_data
import string

with open('/Users/mischadhar/.config/aocd/token/token.txt') as f:
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
    pass

if __name__ == '__main__':

    output_part1 = part1(data)

    print(output_part1)
