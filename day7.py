with open('.\input_files\day7_input') as f:
    lines = f.readlines()
    lines = [int(val) for val in lines[0].split(',')]
#Part1

counter = {}
for val in range(2000):
    fuel = 0
    for i in lines:
        fuel += abs(val-i)

    new_entry = {val: fuel}
    counter.update(new_entry)
result = min(fuel for fuel in counter.values())
print(f'Part1\nMinimum Fule to be used: {result}')

#Part2
counter = {}
for val in range(2000):
    fuel = 0
    for i in lines:
        fuel += sum(range(abs(val-i)+1))

    new_entry = {val: fuel}
    counter.update(new_entry)
result2 = min(fuel for fuel in counter.values())
print(f'Part2\nMinimum Fule to be used: {result2}')
