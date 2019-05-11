import sys
import pandas as pd
import numpy as np

commute_fn = sys.argv[1]

commute = pd.read_csv(commute_fn, index_col=0)

home_str = "Mainly work at or from home"
no_fixed_str = "No fixed place"
offshore_str = "Offshore installation"
outside_str = "Outside UK"

#ignore the "offshore" and "outside UK" population 
commute = commute.drop([offshore_str, outside_str])

total = commute.sum()

#remove the population that stays at home or has no fixed place
outgoing = commute.drop([home_str, no_fixed_str])

#check whether the row and column names are identical,
#as after dropping the special cases (home, no_fixed, offshore, outside),
#only place names should be left
if not all(outgoing.index == outgoing.columns):
    sys.exit("row and column names differ")

#put diagonal values to zero, these represent commute *within* the district, 
#and should not be counted for inter-commute statistics
np.fill_diagonal(outgoing.values, 0)

total_outgoing = outgoing.sum()

perc = total_outgoing/total.values

perc = perc.reset_index().rename(columns={'index':'district', 0:'percentage_outgoing'})
perc.to_csv(sys.stdout, index=False)
