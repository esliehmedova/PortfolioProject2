-- 1
select 	sum(new_cases) as total_cases, sum(new_deaths) as total_deaths, (sum(new_deaths)/sum(new_cases))*100
as DeathPercentage
from portfolioprojects.coviddeaths
where continent is not null
order by 1,2;

-- 2
select 	location, sum(new_deaths) as TotalDeathCount
from portfolioprojects.coviddeaths
where continent is null
and location not in('World', 'European Union', 'International')
group by location
order by TotalDeathCount desc;

-- 3
select 	location, population, max(total_cases) as HighestInfectionCount, Max((total_cases/population))*100 as PercentPopulationInfected
from portfolioprojects.coviddeaths
group by location, population
order by PercentPopulationInfected desc;

-- 4
select 	location, population, date, max(total_cases) as HighestInfectionCount, Max((total_cases/population))*100 as PercentPopulationInfected
from portfolioprojects.coviddeaths
group by location, population, date
order by PercentPopulationInfected desc; 




 


