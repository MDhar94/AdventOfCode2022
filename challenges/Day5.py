from aocd import get_data
from params import LOCAL_TOKEN_PATH

with open(LOCAL_TOKEN_PATH+'token.txt') as f:
    token = f.read().strip('\n')

# Update 'get_data' params to get the desired day's data
data = get_data(session=token,day=5,year=2022)

data = data.split(sep='\n')

Stacks = [['T', 'P', 'Z', 'C', 'S', 'L', 'Q', 'N'],
['L', 'P', 'T', 'V', 'H', 'C', 'G'],
['D', 'C', 'Z', 'F'],
['G', 'W', 'T', 'D', 'L', 'M', 'V', 'C'],
['P', 'W', 'C'],
['P', 'F', 'J', 'D', 'C', 'T', 'S', 'Z'],
['V', 'W', 'G', 'B', 'D'],
['N', 'J', 'S', 'Q', 'H', 'W'],
['R', 'C', 'Q', 'J', 'S', 'L', 'V']]

def part1(data):

    data_instructions = data[10:]

    for instruction in data_instructions:

        tmp = instruction.split()

        moves_ = int(tmp[1])
        from_ = int(tmp[3])
        to_ = int(tmp[5])

        for i in range(moves_):

            to_move = Stacks[from_-1].pop()
            Stacks[to_-1].append(to_move)

    final_items = [stack[-1:] for stack in Stacks]

    return final_items

def part2(data):

    data_instructions = data[10:]

    for instruction in data_instructions:

        tmp = instruction.split()
        moves_ = int(tmp[1])
        from_ = int(tmp[3])
        to_ = int(tmp[5])

        bottom_crate = (len(Stacks[from_-1]) - moves_)
        crates_ = Stacks[from_-1][bottom_crate:]
        Stacks[from_-1] = Stacks[from_-1][:bottom_crate]

        for crate in crates_:
            Stacks[to_-1].append(crate)

    final_items = [stack[-1:] for stack in Stacks]

    return final_items


if __name__ == '__main__':

    part1_output = part1(data)

    part2_output = part2(data)


    print(f'Solution 1:\n{part1_output}\nSolution 2:\n{part2_output}')
