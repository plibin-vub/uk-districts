import pandas as pd

import sys

commute_matrix_fn = sys.argv[1]
region_csv_fn = sys.argv[2]

commute_matrix_df = pd.read_csv(commute_matrix_fn, index_col=0)
region_df = pd.read_csv(region_csv_fn)

to_drop = set(commute_matrix_df.columns) - set(region_df['district'])

commute_matrix_df = commute_matrix_df.drop(to_drop, axis=1)
commute_matrix_df = commute_matrix_df.drop(to_drop)

sys.stdout.write(commute_matrix_df.to_csv())
