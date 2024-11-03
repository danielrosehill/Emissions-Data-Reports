import pandas as pd

df = pd.read_csv('2023-oil-and-gas-monetised.csv')  # or your data source

column_pairs = [
    ('scope_1', 'scope1_mon'), 
    ('scope_2', 'scope2_mon'),        
    ('scope1_and_2', 'scope12_mon'),
    ('scope_3', 'scope3_mon'),
    ('scope_1_2_3', 'scope123_mon')
]

multiplier = 236

for source_col, target_col in column_pairs:
    df[target_col] = df[source_col] * multiplier

input_filename = '2023_oilgas_blank.csv'
output_filename = input_filename.replace('.csv', '_ifvimonetised.csv')


df.to_csv(output_filename, index=False)