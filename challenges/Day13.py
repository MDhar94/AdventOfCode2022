from aocd import get_data
from params import LOCAL_TOKEN_PATH
import ast
from functools import cmp_to_key
from math import prod

with open(LOCAL_TOKEN_PATH+'token.txt') as f:
    token = f.read().strip('\n')

# Update 'get_data' params to get the desired day's data
data = get_data(session=token,day=13,year=2022)

def cmp(l, r):
    match l, r:
        case int(), int():  return (l>r) - (l<r)
        case int(), list(): return cmp([l], r)
        case list(), int(): return cmp(l, [r])
        case list(), list():
            for z in map(cmp, l, r):
                if z: return z
            return cmp(len(l), len(r))

def part1(data):

    data_split = data.split('\n\n')

    packets = [[*map(eval, x.split())] for x in data_split]

    return sum(i for i, p in enumerate(packets, 1) if cmp(*p) == -1)



def part2(data):

    data_split = data.split('\n\n')

    packets = [[*map(eval, x.split())] for x in data_split]

    packets = sorted(sum(packets, [[2], [6]]), key=cmp_to_key(cmp))

    return prod(i for i, p in enumerate(packets, 1) if p in [[2], [6]])

if __name__ == '__main__':

    output1 = part1(data)
    output2 = part2(data)

    print(f"Solution to part 1: {output1}\nSolution to part 2: {output2}")
