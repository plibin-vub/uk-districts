##Census data (2017)
* For the England/Wales dataset, the relevant tab of the raw census data in XLS file format, was exported to england_wales.census.csv. 
* For the Scotland dataset, the relevant tab of the raw census data in XLS file format, was exported to scotland.census.csv.
* From these CSV files, a dataset with age information per district was compiled: england_wales.districts.census.csv and scotland.districts.census.csv. (Details on how these files were constructed can be find below). 
* The English/Welsh data was downloaded from: https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/middlesuperoutputareamidyearpopulationestimates
* The Scotish data was downloaded from: https://www.nrscotland.gov.uk/statistics-and-data/statistics/statistics-by-theme/population/population-estimates/mid-year-population-estimates/population-estimates-time-series-data
* A copy of the raw dataset is stored in census/2011/raw and census/2017/raw.

##English/Welsh census data to districts
The English/Welsh census data contains age-specific data for the sub-regions, and a summary for the district. To construct england_wales.districts.census.csv, we can thus grep for these summary lines:
csvgrep -c 'Area Names' -r "^$" -i england_wales.census.csv > england_wales.districts.census.csv

##Scotish census data to districts
The Scotish census dataset contains age-specific data for the sub-regions that make up the district, but no summary line per district. Therefore, we sum all the sub-regions per district, using python pandas:
scot = pd.read_csv("scotland.census.csv")
districts = scot.groupby("Council Area").sum()
districts.to_csv("scotland.districts.census.csv")

##GB census data per district
csvstack scotland.districts.census.csv england_wales.districts.census.csv > gb.districts.census.csv

##Differences between census and commute data structure
* In the commute dataset, Westminster and City of London is merged
* In the commute dataset, there is no district "Isles of Scilly" 
