import pandas as pd

input_path = '2023_oilandgas_blank.csv'
output_path = input_path.replace('.csv', '_ifvi_mon.csv')

df = pd.read_csv(input_path)

column_pairs = {
    'scope_1': 'scope1_mon',
    'scope_2': 'scope2_mon',
    'scope1_and_2': 'scope12_mon',
    'scope_3': 'scope3_mon',
    'scope_1_2_3': 'scope123_mon'
}

for source, target in column_pairs.items():
    if source in df.columns:
        df[target] = df[source] * 236_000_000

df.to_csv(output_path, index=False)