import pandas as pd
#data = list(map(str,input('enter input').split()))

df = pd.read_csv('.\input_files\day3_input.csv',dtype=str)

# part1
gamma = ''
epsilon = ''
t = df.input.count()/2
for i in range(len(df.input[0])):
    if df.input.map(lambda x: int(x[i])).sum() < t:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon +='0'

power_consumption = int(gamma,2) * int(epsilon,2)
print(f'Part1\npower onsumption: {power_consumption}\n')


#part2
oxy = df
for i in range(len(oxy.input[0])):
    ones = oxy.input.map(lambda x: int(x[i])).sum()
    totals = oxy.input.map(lambda x: int(x[i])).count()
    perc = ones/totals

    if perc < .5:
        oxy = oxy[oxy.input.map(lambda x: int(x[i]) == 0)]
    else:
        oxy = oxy[oxy.input.map(lambda x: int(x[i]) == 1)]
oxygen_generator = int(oxy.input.values[0],2)
#CO2

co2 = df

for i in range(len(co2.input[0])):

    ones = co2[co2.input.map(lambda x: int(x[i]) == 1)].count().values[0]
    zeros = co2[co2.input.map(lambda x: int(x[i]) == 0)].count().values[0]

    if zeros+ones == 1:
        break
    elif zeros <= ones:

        co2 = co2[co2.input.map(lambda x: int(x[i]) == 0)]
    else:

        co2 = co2[co2.input.map(lambda x: int(x[i]) == 1)]
co2_scrubber = int(co2.input.values[0],2)

life_support_rating = oxygen_generator*co2_scrubber
print(f'Part2\nLife Support Rating: {life_support_rating}')
