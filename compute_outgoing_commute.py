import sys
import pandas as pd
import numpy as np

commute_fn = sys.argv[1]

commute = pd.read_csv(commute_fn, index_col=0)

#check whether the row and column names are identical
if not all(commute.index == commute.columns):
    sys.exit("row and column names differ")

#put diagonal values to zero, these represent commute *within* the district, 
#and should not be counted for inter-commute statistics
np.fill_diagonal(commute.values, 0)

total = commute.sum(axis=1)
total = total.reset_index().rename(columns={'index':'district', 0:'total'})
total.to_csv(sys.stdout, index=False)
