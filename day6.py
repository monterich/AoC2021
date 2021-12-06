from collections import defaultdict

with open('.\input_files\day6_input') as f:
    lines = f.readlines()
    lines = [int(val) for val in lines[0].split(',')]

#Part1
for i in range(80):

    for pos in range(len(lines)):
        if lines[pos] == 0:
            lines[pos] = 6
            lines.append(8)
        else:
            lines[pos] -= 1

result = len(lines)
print(f'Part1\n# of Fish after 80 days: {result}')

#part2
with open('.\input_files\day6_input') as f:
    lines = f.readlines()
    lines = [int(val) for val in lines[0].split(',')]
    fish_dict = defaultdict(int)
    for line in lines:
        fish_dict[int(line)] +=1


for i in range(256):
    new_fish_dict = defaultdict(int)
    for fish_age in fish_dict:
        if fish_age == 0:
            new_fish_dict[6] += fish_dict[fish_age]
            new_fish_dict[8] = fish_dict[fish_age]
        else:
            new_fish_dict[fish_age-1] += fish_dict[fish_age]
    fish_dict = new_fish_dict

result2 = 0
for fish in fish_dict:
    result2 += fish_dict[fish]

print(f'Part2\n # Fish after 256 days: {result2}')

#result2 = len(lines)
#print(f'Part2\n# of Fish after 256 days: {result2}')