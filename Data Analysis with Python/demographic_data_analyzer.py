import pandas as pd

def calculate_demographic_data(print_data=True):
   
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()
    
    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Percentage of people who have a Bachelor's degree
    percentage_bachelors = round((len(df[df['education'] == 'Bachelors']) / len(df)) * 100, 1)

    # Advanced education filters
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # Percentages with salary >50K
    higher_education_rich = round((len(df[higher_education & (df['salary'] == '>50K')]) / len(df[higher_education])) * 100, 1)
    lower_education_rich = round((len(df[lower_education & (df['salary'] == '>50K')]) / len(df[lower_education])) * 100, 1)

    # Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # Percent rich among minimum hour workers
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers)) * 100, 1)

    # Country with highest percentage of >50K
    total_people = df.groupby('native-country').size()
    rich_people = df[df['salary'] == '>50K'].groupby('native-country').size()
    country_rich_percentage = (rich_people / total_people) * 100

    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)
    highest_earning_country = country_rich_percentage[country_rich_percentage == country_rich_percentage.max()].index[0]

    # Most popular occupation in India (>50K)
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    occupation_counts = india_rich.groupby('occupation').size()
    top_IN_occupation = occupation_counts[occupation_counts == occupation_counts.max()].index[0]

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
