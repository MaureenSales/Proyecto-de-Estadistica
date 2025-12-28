# Share of deaths from violence in non-state societies - Data package

This data package contains the data that powers the chart ["Share of deaths from violence in non-state societies"](https://ourworldindata.org/grapher/share-of-violent-deaths-non-state-societies?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website. It was downloaded on December 28, 2025.

### Active Filters

A filtered subset of the full data was downloaded. The following filters were applied:

## CSV Structure

The high level structure of the CSV file is that each row is an observation for an entity (usually a country or region) and a timepoint (usually a year).

The first two columns in the CSV file are "Entity" and "Code". "Entity" is the name of the entity (e.g. "United States"). "Code" is the OWID internal entity code that we use if the entity is a country or region. For normal countries, this is the same as the [iso alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the entity (e.g. "USA") - for non-standard countries like historical countries these are custom codes.

The third column is either "Year" or "Day". If the data is annual, this is "Year" and contains only the year as an integer. If the column is "Day", the column contains a date string in the form "YYYY-MM-DD".

The final column is the data column, which is the time series that powers the chart. If the CSV data is downloaded using the "full data" option, then the column corresponds to the time series below. If the CSV data is downloaded using the "only selected data visible in the chart" option then the data column is transformed depending on the chart type and thus the association with the time series might not be as straightforward.

## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc.. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc..

## About the data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stich together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

## Detailed information about the data


## Share of violent deaths (non-state societies)
Percentage of deaths due to murder or war per year in non-state societies.


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Bowles, S. (2009), Gat, A. (2008), Knauft, B. M. et al (1987), Keeley, L. H. (1996), Pinker, S. (2011), and Walker, R. S., & Bailey, D. H. (2013) – processed by Our World in Data

#### Full citation
Bowles, S. (2009), Gat, A. (2008), Knauft, B. M. et al (1987), Keeley, L. H. (1996), Pinker, S. (2011), and Walker, R. S., & Bailey, D. H. (2013) – processed by Our World in Data. “Share of violent deaths (non-state societies)” [dataset]. Bowles, S. (2009), Gat, A. (2008), Knauft, B. M. et al (1987), Keeley, L. H. (1996), Pinker, S. (2011), and Walker, R. S., & Bailey, D. H. (2013) [original data].
Source: Bowles, S. (2009), Gat, A. (2008), Knauft, B. M. et al (1987), Keeley, L. H. (1996), Pinker, S. (2011), and Walker, R. S., & Bailey, D. H. (2013) – processed by Our World In Data

### Additional information about this data
This dataset contains estimates of the frequency of violent deaths due to murder or war in modern and prehistoric state and non-state societies, based on archaeological and ethnographic evidence.

For modern state societies, homicide rates are routinely published by statistical offices or other state agencies, and reliable data on war deaths are published by research institutes. For non-state societies, we generally have two different sources of information: for the more recent past (since the late 19th century), abundant ethnographic evidence is available; for the more distant past, we have evidence from archaeological sites and skeletal remains.

The main sources for this dataset are as follows:
- Bowles (2009) – Did Warfare Among Ancestral Hunter-Gatherers Affect the Evolution of Human Social Behaviors?. In Science, 324, 5932, 1293–1298.
- Gat (2006) – War in Human Civilization. Oxford University Press, USA.
- Knauft, Bruce M. et al (1987) – Reconsidering Violence in Simple Human Societies: Homicide among the Gebusi of New Guinea. In Current Anthropology, 28, 4, 457-500.
- Keeley (1997) – War Before Civilization: The Myth of the Peaceful Savage. Oxford University Press, USA.
- Pinker (2011) – The Better Angels of Our Nature: Why Violence Has Declined. Viking.
- Walker and Bailey (2013) – Body counts in lowland South American violence. In Evolution and Human Behavior, 34, 1, 29–34.


    