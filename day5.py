import pandas as pd

df = pd.read_csv('.\input_files\day5_input',dtype=str,header=None,delimiter="->")
df_a = df.iloc[:,0].str.split(',',expand=True)
df_b = df.iloc[:,1].str.split(',',expand=True)
df_a.columns = ['x1','y1']
df_b.columns = ['x2','y2']
df = pd.concat([df_a, df_b], axis=1, ignore_index=False)
df = df.astype('int')

#Part1
df['line'] = ''
for i in range(500):
    if df.loc[i].x1 == df.loc[i].x2:
        df['line'].loc[i] = [[df.loc[i].x1,pos] for pos in range(min(df['y1'].loc[i],df['y2'].loc[i]),max(df['y1'].loc[i],df['y2'].loc[i])+1)]
    elif df.loc[i].y1 == df.loc[i].y2:
        df['line'].loc[i] = [[pos,df.loc[i].y1] for pos in range(min(df['x1'].loc[i],df['x2'].loc[i]),max(df['x1'].loc[i],df['x2'].loc[i])+1)]
    else:
        continue

lines = {}
for l in range(500):
    for i in df.loc[l].line:
        if str(i) in lines:
            lines[str(i)] +=1
        else:
            new_point = {str(i):1}
            lines.update(new_point)

result = sum(value > 1 for value in lines.values())
print(f'Part1\nIntersecting lines vertical & horizontal: {result}')

#Part2
point_sum = []
for l in df[df.line == ''].index:

    max_val = max(df.loc[l].x1,df.loc[l].x2)
    min_val = min(df.loc[l].x1,df.loc[l].x2)

    x1 = df.loc[l].x1
    x2 = df.loc[l].x2
    y1 = df.loc[l].y1
    y2 = df.loc[l].y2
    coordinates = []

    if (x1>x2 and y1>y2):
        for i in range(0,max_val-min_val+1,1):
            new_coordinates = [x1-i,y1-i]
            coordinates.append(new_coordinates)
    elif (x1>x2 and y1<y2):
        for i in range(0,max_val-min_val+1,1):
            new_coordinates = [x1-i,y1+i]
            coordinates.append(new_coordinates)
    elif (x1<x2 and y1>y2):
        for i in range(0,max_val-min_val+1,1):
            new_coordinates = [x1+i,y1-i]
            coordinates.append(new_coordinates)
    elif (x1<x2 and y1<y2):
        for i in range(0,max_val-min_val+1,1):
            new_coordinates = [x1+i,y1+i]
            coordinates.append(new_coordinates)
    else:
            new_coordinates = []
            coordinates.append(new_coordinates)

    point_sum.append(coordinates)

for line in point_sum:
    for point in line:
        if str(point) in lines:
            lines[str(point)]+=1
        else:
            new_point = {str(point):1}
            lines.update(new_point)

result2 = sum(value > 1 for value in lines.values())
print(f'Part2\nIntersecting Lines all directions: {result2}')