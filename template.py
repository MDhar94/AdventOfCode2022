from aocd import get_data
from params import LOCAL_TOKEN_PATH

with open(LOCAL_TOKEN_PATH+'token.txt') as f:
    token = f.read().strip('\n')

# Update 'get_data' params to get the desired day's data
# data = get_data(session=token,day=,year=2022)

def part1(data):
    pass

def part2(data):
    pass

if __name__ == '__main__':
    pass
