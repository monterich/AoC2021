import pandas as pd
df = pd.read_csv('.\input_files\day1_input.csv')


# part1
def counter(X):
    count = 0
    for m in range(1, len(X)):
        if X[m] > X[m - 1]:
            count += 1
        else:
            continue
    return count

result1 = counter(df.input)
print(f'Day1 \nResult Part1: {result1}')

# part 2
def sliding_counter(X):
    count = 0
    max_val = len(X)-3
    m = 1

    while m <= max_val:
        a = X[X.index.isin([i for i in range(m,m+3)])].sum()
        b = X[X.index.isin([i for i in range(m-1,m+2)])].sum()
        if a > b:
            count += 1
        else:
            count += 0
        m += 1
    return count

result2 = sliding_counter(df.input)
print(f'Result Part2: {result2} ')