import pandas as pd
import sys

commute_fn = sys.argv[1]
northern_ireland_fn = sys.argv[2]

commute = pd.read_csv(commute_fn, index_col=0)
northern_ireland = pd.read_csv(northern_ireland_fn)

special_fields = ['Mainly work at or from home', 'No fixed place', 'Offshore installation', 'Outside UK']

commute = commute.drop(special_fields)

#after removing these special fields,
#the commute matrix is a square matrix, 
#so we remove the North-Irish districts from the rows and columns 
commute = commute.drop(northern_ireland['district'])
commute = commute.drop(northern_ireland['district'], axis=1)

print(commute.to_csv())
