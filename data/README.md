# Data 

## OutbreaksData.csv
Grabbed from [this paper](https://www.nature.com/articles/s41597-022-01797-2) this csv contains every outbreak from 1996-2022 including

- Year of outbreak
- Type of outbreak (environmental, etc.)
- Country
- Number infected (used as a proxy for scale of outbreak)

## P_Data_Extract_From_Health_Nutrition_and_Population_Statistics
Grabbed from the [world data bank](https://databank.worldbank.org/source/health-nutrition-and-population-statistics).
Includes country-level statistics for each year since 1960 (although the data gets less complete as we go back in time) including:

- Hospital beds per 1,000 people
- Human capital index
- GNI per capita (using the Atlas method)
- Low birthweight babies as a % of births
- Number of surgical procedures per 100,000
- People practicing open defecation as a % of the population
- People using at least basic drinking water services as a % of the population
- People using at least basic sanitation services as a % of the population
- People using safely managed sanitation services as a % of the population
- People with basic handwashing facilities including soap and water
- Physicians per 1,000 people
- Prevalence of undernourishment as a % of the population
- Specialist surgical workforce per 100,000 people

These statistics were chosen because they appear to be good proxies for trends in health infrastrucutre, rural access to sanitation, and basic economic indicators. The full list of statistics from the world bank is much broader, though, and we encourage any contributor to look at the original dataset.

## historical_outbreaks.txt
This is a text file containing the summary found in [this paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7120709/) of recorded zoonotic disease outbreaks through history. We took the summary and turned it into a dataframe containing the following columns:
- Year of outbreak
- Affected country ISO-3 code
- Affected country name
- Description of outbreak
- Years since country's last outbreak
- Source (sometimes who reported the outbreak, sometimes the country in which it started)

The summary text is not consistent in its formatting and the types of information that each entry contains, but it tells a compelling story over time that we decided to visualize for our report. We employed a rigorous data cleaning process to create the dataframe that can by found in Historical_Data_Cleaning.ipynb
