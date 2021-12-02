import pandas as pd

df = pd.read_csv('day1_input.csv')
print(df.input.count())
print(df.head())

# part1
def counter(X):
    count = 0
    for m in range(1, len(X)):
        if X[m] > X[m - 1]:
            count += 1
        else:
            continue
    return count
