from aocd import get_data
from params import LOCAL_TOKEN_PATH

with open(LOCAL_TOKEN_PATH+'token.txt') as f:
    token = f.read().strip('\n')

# Update 'get_data' params to get the desired day's data
data = get_data(session=token,day=6,year=2022)

def part1(data):

    for i in range(len(data)-4):

        window = data[i:i+4]

        if len(list(set(window).intersection(window))) == 4:

            output = i+4
            break

    return output



def part2(data):

    for i in range(len(data)-14):

        window = data[i:i+14]

        if len(list(set(window).intersection(window))) == 14:

            output = i+14
            break

    return output

if __name__ == '__main__':

    part1_output = part1(data)
    part2_output = part2(data)

    print(f'Part 1 solution:\n{part1_output}\nPart 2 solution:\n{part2_output}')
