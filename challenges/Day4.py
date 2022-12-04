from aocd import get_data
from params import LOCAL_TOKEN_PATH

import re

with open(LOCAL_TOKEN_PATH+'token.txt') as f:
    token = f.read().strip('\n')

# Update 'get_data' params to get the desired day's data
data = get_data(session=token,day=4,year=2022)

def part1(data):

    data = data.split(sep='\n')

    answer_count = 0

    for area in data:

        split = re.split(',| |\-', area)

        elf1 = [int(x) for x in split[:2]]
        elf2 = [int(x) for x in split[2:]]

        # Need to '+1' on range end to include lists of n=1
        # otherwise they return empty lists which are included as subsets
        range1 = list(range(elf1[0],elf1[1]+1))
        range2 = list(range(elf2[0],elf2[1]+1))

        if set(range1).issubset(range2) or set(range2).issubset(range1):

            answer_count += 1

    return print(answer_count)


def part2(data):
    pass

if __name__ == '__main__':

    part1(data)
