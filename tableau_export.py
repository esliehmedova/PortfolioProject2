
import pandas as pd
from sqlalchemy import create_engine

# Replace with your own MySQL username and password
engine = create_engine("mysql+pymysql://user:password@localhost:3306/portfolioprojects")

queries = {
    # Table 1: global numbers
    "Tableau_table1": """
        select 	sum(new_cases) as total_cases, sum(new_deaths) as total_deaths, (sum(new_deaths)/sum(new_cases))*100
        as DeathPercentage
        from portfolioprojects.coviddeaths
        where continent is not null
        order by 1,2;
    """,

    # Table 2: total deaths per continent
    "Tableau_table2": """
        select 	location, sum(new_deaths) as TotalDeathCount
        from portfolioprojects.coviddeaths
        where continent is null
        and location not in('World', 'European Union', 'International')
        group by location
        order by TotalDeathCount desc;
    """,

    # Table 3: percent of population infected per country (for the map)
    "Tableau_table3": """
        select 	location, population, max(total_cases) as HighestInfectionCount, Max((total_cases/population))*100 as PercentPopulationInfected
        from portfolioprojects.coviddeaths
        group by location, population
        order by PercentPopulationInfected desc;
    """,

    # Table 4: same as table 3, but per date (for the line chart)
    "Tableau_table4": """
        select 	location, population, date, max(total_cases) as HighestInfectionCount, Max((total_cases/population))*100 as PercentPopulationInfected
        from portfolioprojects.coviddeaths
        group by location, population, date
        order by PercentPopulationInfected desc; 
    """,
}

for name, query in queries.items():
    df = pd.read_sql(query, engine)
    df = df.fillna(0)  # same as replacing empty cells with 0 in Excel
    df.to_excel(f"{name}.xlsx", index=False)
    print(f"{name}.xlsx saved: {len(df)} rows")
    print(df.head(3), "\n")
