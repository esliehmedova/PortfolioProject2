# COVID-19 Dashboard (Tableau)

An interactive Tableau dashboard built on the results of my SQL data exploration project. It shows global COVID-19 totals, deaths by continent, and how much of each country's population was infected, on a map and over time.

**Interactive dashboard:** [View on Tableau Public]([paste-your-link-here](https://public.tableau.com/app/profile/asli.ahmedova/viz/Covid_dashboard_17923298625910/Dashboard1))

![Dashboard preview](dashboard.png)

## Tools

- **MySQL** – queries that prepare the data for each chart
- **Python (pandas + SQLAlchemy)** – exports the query results to Excel files
- **Tableau Public** – charts and dashboard

## How it works

1. The queries in `queries_for_tableau.sql` run on the `coviddeaths` table in MySQL.
2. `tableau_export.py` runs the same queries and saves each result as an Excel file.
3. The four Excel files are loaded into Tableau Public as data sources, one per chart.

## Files

| File | Contents |
|---|---|
| `queries_for_tableau.sql` | The four SQL queries behind the dashboard |
| `tableau_export.py` | Python script that exports the query results to Excel |
| `Tableau_table1.xlsx` | Global numbers: total cases, total deaths, death percentage |
| `Tableau_table2.xlsx` | Total deaths per continent |
| `Tableau_table3.xlsx` | Highest infection count and percent of population infected per country |
| `Tableau_table4.xlsx` | Same as table 3, by date |
| Tableau dashboard | Published on Tableau Public (link above) |

## The dashboard

- **Global numbers** – total cases, total deaths and death percentage worldwide
- **Total deaths per continent** – bar chart comparing continents
- **Percent population infected per country** – world map, colored by infection rate
- **Percent population infected over time** – line chart for selected countries

## Key findings

The data covers the period up to the end of April 2021.

- About **150.6 million** cases and **3.18 million** deaths worldwide, a death percentage of about **2.1%**
- **Europe** had the highest total death count of all continents, followed by North America and South America
- **Andorra** had the highest share of its population infected, at about **17.1%**

## Running it yourself

1. Load the COVID data into MySQL (see my SQL data exploration project).
2. Install the libraries: `pip install pandas sqlalchemy pymysql openpyxl`
3. In `tableau_export.py`, replace `user:password` with your own MySQL username and password.
4. Run `python tableau_export.py` to create the four Excel files.
5. Connect them in Tableau Public.

## Lessons learned

- **Copying results into Excel can break the numbers.** With non-English regional settings, Excel read the dot in `1.0003` as a thousands separator and turned it into a huge number, while values below 1 were kept as text. In Tableau this caused a "numeric overflow" error. Exporting the results with pandas kept the decimals correct.
- **Dimensions vs. measures.** Tableau showed the damaged column as text (a dimension, above the line) instead of a number (a measure, below the line). Checking where each field appears is a quick way to spot data type problems.
- **No row limit.** MySQL Workbench limits how many result rows you can copy. The Python export has no such limit, which mattered for table 4 with over 85,000 rows.
