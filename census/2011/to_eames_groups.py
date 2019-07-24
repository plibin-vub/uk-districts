import pandas as pd
import sys
from argparse import ArgumentParser
import numpy as np

parser = ArgumentParser(description="to_eames_groups")
parser.add_argument("--census-fn", dest="census_fn", type=str, required=True)
args = parser.parse_args()

df = pd.read_csv(args.census_fn, index_col=0)

def merge(df_, regions, new_region):
    df_ = df_.rename({k:new_region for k in regions})
    df_ = df_.groupby(level=0).sum()
    return df_

#split the 18-19 age group in 2 columns
df['Age 18'] = np.ceil(df['Age 18 to 19']/2)
df['Age 19'] = np.ceil(df['Age 18 to 19']/2)

df['Children'] = df['Age 0 to 4']
df['Adolescents'] = \
    df['Age 5 to 7'] + df['Age 8 to 9'] + df['Age 10 to 14'] + \
    df['Age 15'] + df['Age 16 to 17'] + df['Age 18']
df['Adults'] = \
    df['Age 19'] + df['Age 20 to 24'] + df['Age 25 to 29']  + \
    df['Age 30 to 44'] + df['Age 45 to 59'] + df['Age 60 to 64']
df['Elderly'] = \
    df['Age 65 to 74'] + df['Age 75 to 84'] + df['Age 85 to 89'] + \
    df['Age 90 and over']

age_columns = filter(lambda x: x.startswith('Age '), list(df))
df = df.drop(list(age_columns), axis=1)

df = df.drop(["Isles of Scilly"])
df = merge(df, ["Westminster", "City of London"], "Westminster+City of London")

df.to_csv(sys.stdout)
