import json
import pandas as pd
import getpass

username = getpass.getuser()

# open and read the JSON file
with open('questions_raw.json', 'r') as file:
    data = json.load(file)

df = pd.DataFrame(data)
df = df[~df['question'].str.contains(r'[<>]', regex=True)]

df['question'] = df['question'].str.strip("'")
df['value'] = df['value'].str.strip("$")
df['answer'] = df['answer'].str.replace(r'\\', '', regex=True)
df['id'] = range(1, len(df) + 1)
df['used'] = 'N'

col = df.pop('id')
df.insert(0, 'id', col)

col = df.pop('used')
df.insert(1, 'used', col)

col = df.pop('air_date')
df.insert(len(df.columns)-1, 'air_date', col)

df.to_csv('test.csv', index=False)



