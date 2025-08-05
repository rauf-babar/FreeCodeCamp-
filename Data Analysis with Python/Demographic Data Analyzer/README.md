# Demographic Data Analyzer

This project analyzes demographic data from the 1994 U.S. Census using Python and Pandas. The goal is to generate insights about age, education, work hours, income, and occupations.

## Key Insights Produced

- Distribution of population across races
- Average age of men
- Share of people with a Bachelor's degree
- Income comparisons between advanced and non-advanced education groups
- Minimum weekly work hours and income share among those workers
- Country with the highest proportion of high earners
- Most common occupation among high earners in India

All results are rounded to the nearest tenth.

## Example Output

```
Number of each race:
White                 27816
Black                  3124
Asian-Pac-Islander     1039
Amer-Indian-Eskimo      311
Other                   271
Average age of men: 39.4
Percentage with Bachelors degrees: 16.4%
Percentage with higher education that earn >50K: 46.5%
Percentage without higher education that earn >50K: 17.4%
Min work time: 1 hours/week
Percentage of rich among those who work fewest hours: 10.0%
Country with highest percentage of rich: Iran
Highest percentage of rich people in country: 41.9%
Top occupations in India: Prof-specialty
```

## Installation

Make sure Python and Pandas are installed:

```bash
python --version
pip install pandas
```

## Usage

Place `adult.data.csv` in the same directory as the script and run:

```bash
python main.py
```

## Dataset Source

Dua, D. and Graff, C. (2019).  
UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science.  
[https://archive.ics.uci.edu/](https://archive.ics.uci.edu/)
