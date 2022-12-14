from aocd import get_data
from params import LOCAL_TOKEN_PATH
import matplotlib.pyplot as plt

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
    pass

def part2(data):
    pass

if __name__ == '__main__':

    display_map(data)
