from aocd import get_data
from params import LOCAL_TOKEN_PATH

import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

with open(LOCAL_TOKEN_PATH+'token.txt') as f:
    token = f.read().strip('\n')

# Update 'get_data' params to get the desired day's data
data = get_data(session=token,day=14,year=2022)

def display_map(data):

    data_split = data_split = data.split('\n')

    fig = plt.figure(figsize=(8,8))
    plt.gca().invert_yaxis()

    for formation in data_split:
        ridge = list(map(eval,formation.split(' -> ')))

        for i in range(len(ridge) - 1):
            x1,y1,x2,y2 = ridge[i][0],ridge[i][1],ridge[i+1][0],ridge[i+1][1]

            for y in range(min(y1,y2),max(y1,y2)+1):
                    for x in range(min(x1,x2),max(x1,x2)+1):

                        plt.plot(x,y,marker='s',color='black')

    return plt.show()

def part1(data):

    data_split = data.split('\n')
    cave_data = defaultdict(lambda: '.')

    for formation in data_split:
        ridge = [complex(*map(int, pair.split(','))) for pair in formation.split(' -> ')]

        for i in range(len(ridge) -1):
            difference = ridge[i+1] - ridge[i]
            diff_x = int(difference.real)
            diff_y = int(difference.imag)

            if np.sign(diff_x):
                for dx in range(0,diff_x+np.sign(diff_x),np.sign(diff_x)):
                    cave_data[ridge[i]+dx] = '#'

            if np.sign(diff_y):
                for dy in range(0,diff_y+np.sign(diff_y),np.sign(diff_y)):
                    cave_data[ridge[i]+dy*1j] = '#'

    class Cave:
        def __init__(self, cave_array):
            self.cave_array = cave_array
            self.rock_list = [rock for rock in self.cave_array.keys() if self.cave_array[rock] == '#']
            self.lowest_rock = max(self.rock_list, key=lambda z: z.imag).imag
            self.leftest_rock = min(self.rock_list, key=lambda z: z.real).real
            self.rightest_rock = max(self.rock_list, key=lambda z: z.real).real
            self.sand_position = 500
            self.sand_quantity = 0

        def move_sand(self):
            if self.cave_array[self.sand_position + 1j] == '.':
                self.cave_array[self.sand_position] = '.'
                self.sand_position += 1j
                self.cave_array[self.sand_position] = 'o'
            elif self.cave_array[self.sand_position - 1 + 1j] == '.':
                self.cave_array[self.sand_position] = '.'
                self.sand_position += -1 + 1j
                self.cave_array[self.sand_position] = 'o'
            elif self.cave_array[self.sand_position + 1 + 1j] == '.':
                self.cave_array[self.sand_position] = '.'
                self.sand_position += 1 + 1j
                self.cave_array[self.sand_position] = 'o'
            else:
                self.sand_position = 500
                self.sand_quantity += 1

        def sand_loop(self):
            while (self.sand_position.imag < self.lowest_rock and
                    self.leftest_rock <= self.sand_position.real <= self.rightest_rock):
                self.move_sand()
            return self.sand_quantity

    cave = Cave(cave_data)

    return cave.sand_loop()


def part2(data):
    pass

if __name__ == '__main__':

    # display_map(data)

    output1 = part1(data)

    print(f"Solution to part 1: {output1}")
