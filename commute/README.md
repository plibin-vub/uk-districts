# Commute data
* Census data was available on the district level (2011), for the entire UK, from the dataset WU03UK at https://www.nomisweb.co.uk
* A query to obtain the required fields from WU03UK, was formulated after personal communication with the support service of NOMIS (commute/NOMIS-commute-emails.pdf), the description of the query is in commute/query.txt
* a UK commute matrix was stored in uk.matrix.csv, which contains:
  - interactions between all districts (including Northern-Ireland)
  - special fields: "Mainly work at or from home", "No fixed place", "Offshore installation", "Outside UK"
* to obtain a GB commute matrix (i.e., without Northern-Ireland), without these special fields, run: `commute/mainland\_simple.py uk.matrix.csv > gb-simple.matrix.csv`
* to compute the outgoing commuters per district, use the script commute/compute_outgoing_commute.py
