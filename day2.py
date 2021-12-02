#Day2 Challenge

import pandas as pd
df = pd.read_csv('.\input_files\day2_input.csv')

# part1
df['direction'] = df.input.map(lambda x: x.split()[0])
df['steps'] = pd.to_numeric(df.input.map(lambda x: x.split()[1]))

horizontal = df[df.direction == 'forward'].steps.sum()
up = df[df.direction == 'up'].steps.sum()
down = df[df.direction == 'down'].steps.sum()
depth = down-up
result1 = depth*horizontal
print(f'Day2 \nResult Part1: {result1}')

# part2
def submarine(X):
    aim = 0
    depth = 0
    horizontal = 0

    for i in range(len(X)):
        if X[X.index == i].direction.values[0] == 'forward':
            horizontal += X[X.index == i].steps.values[0]
            depth += X[X.index == i].steps.values[0] * aim

        elif X[X.index == i].direction.values[0] == 'up':
            aim -= X[X.index == i].steps.values[0]
        elif X[X.index == i].direction.values[0] == 'down':
            aim += X[X.index == i].steps.values[0]
        else:
            print('error')
    return depth * horizontal
result2 = submarine(df)
print(f'Results Part2: {result2}')