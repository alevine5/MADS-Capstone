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
