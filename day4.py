import pandas as pd
import numpy as np
df = pd.read_csv('.\input_files\day4_input',dtype=str,header=None)
df = df.iloc[:,0].str.split(expand=True)
df.columns = 'l1 l2 l3 l4 l5'.split()
df = df.astype('int')

#Part1
bingo = [84,28,29,75,58,71,26,6,73,74,41,39,87,37,16,79,55,60,62,80,64,95,46,15,5,47,2,35,32,78,89,90,96,33,4,69,42,30,54,85,65,83,44,63,20,17,66,81,67,77,36,68,82,93,10,25,9,34,24,72,91,88,11,38,3,45,14,56,22,61,97,27,12,48,18,1,31,98,86,19,99,92,8,43,52,23,21,0,7,50,57,70,49,13,51,40,76,94,53,59]
def bingo_winner(d,pos):
    for num in range(5):
        if d.iloc[0:5,num].isna().sum() == 5:

            return 'winner'
        else:
            continue
    for i in range(pos,pos+5,1):
        if d.loc[i].isna().sum() == 5:
            return 'winner'
        else:
            continue

for num in bingo:
    df = df.replace(num,np.nan)

    for i in range(0,500,5):
        new_df = df.loc[i:i+4]

        if bingo_winner(new_df,i) == 'winner':
            last_number = num
            winner_index = i
            result = 'winner'
            break
        else:
            result = 'open'
            continue
    if result == 'winner':
        break
    else:
        continue

winner = df.loc[winner_index:winner_index+4].fillna(0).sum().sum()
result = last_number*winner
print(f'Part1\nBingo Score: {result}\n')

#Part2

win_counter = 0
winners = {0: {'winner_index': np.nan, 'last_number': np.nan, 'board_sum': np.nan}}
winner_list = []

for num in bingo:
    df = df.replace(num, np.nan)

    for i in range(0, 500, 5):
        new_df = df.loc[i:i + 4]

        if i in winner_list:
            continue
        elif bingo_winner(new_df, i) == 'winner':
            win_counter += 1
            last_number = num
            winner_index = i
            board_sum = new_df.fillna(0).sum().sum()
            new_val = {win_counter: {'winner_index': winner_index, 'last_number': last_number, 'board_sum': board_sum}}
            winners.update(new_val)
            winner_list.append(winner_index)
            if win_counter >= 100:
                break
            else:
                continue
        else:
            continue
        if win_counter >= 100:
            break
        else:
            continue

result2 = winners[max(winners)]['last_number']*winners[max(winners)]['board_sum']
print(f'Part2\nLast Board Score: {result2}')