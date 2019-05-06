# uk-districts

##GIS data
* downloaded from https://geoportal.statistics.gov.uk/datasets/local-authority-districts-december-2017-full-clipped-boundaries-in-great-britain/
* copy of the data (29/04/2019) stored at Pieter's Google Drive: https://drive.google.com/open?id=1QC0459uRoO9sUF1hlDJtSPj8ip4FL5VD
* uk.districts.gis.csv is generated from the shape file using the parse_raw.py script

##Commute data
* For England/Wales, census data was available on the district level (2011), and the data was downloaded from https://www.nomisweb.co.uk
* TODO: include commute to Scotland
* a commute matrix was stored in england_wales.commute.csv
* to compute the outgoing commuters per district, use the script compute_outgoing_commute.py

##Census data
* For the England/Wales dataset, the relevant tab of the raw census data in XLS file format, was exported to england_wales.census.csv. 
* For the Scotland dataset, the relevant tab of the raw census data in XLS file format, was exported to scotland.census.csv.
* A copy of the raw dataset is stored at Pieter's Google Drive: https://drive.google.com/open?id=1QC0459uRoO9sUF1hlDJtSPj8ip4FL5VD
* From these CSV files, a dataset with age information per district was compiled: england_wales.districts.census.csv and scotland.districts.census.csv. (Details on how these files were constructed can be find below). 

##English/Welsh census data to districts
The English/Welsh census data contains age-specific data for the sub-regions, and a summary for the district. To construct england_wales.districts.census.csv, we can thus grep for these summary lines:
csvgrep -c 'Area Names' -r "^$" -i england_wales.census.csv > england_wales.districts.census.csv

##Scotish census data to districts
The Scotish census dataset contains age-specific data for the sub-regions that make up the district, but no summary line per district. Therefore, we sum all the sub-regions per district, using python pandas:
scot = pd.read_csv("scotland.census.csv")
districts = scot.groupby("Council Area").sum()
districts.to_csv("scotland.districts.census.csv")
