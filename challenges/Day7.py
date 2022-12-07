from aocd import get_data
from params import LOCAL_TOKEN_PATH
from collections import defaultdict
from itertools import accumulate

with open(LOCAL_TOKEN_PATH+'token.txt') as f:
    token = f.read().strip('\n')

# Update 'get_data' params to get the desired day's data
data = get_data(session=token,day=7,year=2022)

def part1(data):

    data = data.split('\n')

    dirs = defaultdict(int)

    for line in data:
        match line.split():
            case '$', 'cd', '/': curr = ['']
            case '$', 'cd', '..': curr.pop()
            case '$', 'cd', x: curr.append(x+'/')
            case '$', 'ls': pass
            case 'dir', _: pass
            case size, _:
                for p in accumulate(curr):
                    dirs[p] += int(size)

    return sum(s for s in dirs.values() if s <= 100_000)


def part2(data):

    data = data.split('\n')

    dirs = defaultdict(int)

    for line in data:
        match line.split():
            case '$', 'cd', '/': curr = ['']
            case '$', 'cd', '..': curr.pop()
            case '$', 'cd', x: curr.append(x+'/')
            case '$', 'ls': pass
            case 'dir', _: pass
            case size, _:
                for p in accumulate(curr):
                    dirs[p] += int(size)

    return min(s for s in dirs.values() if s >= dirs[''] - 40_000_000)


if __name__ == '__main__':

    part1_output = part1(data)
    part2_output = part2(data)

    print(f'Part 1 solution:\n{part1_output}\nPart 2 solution:\n{part2_output}')
