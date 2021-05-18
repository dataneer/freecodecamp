import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    # header=0 means the first row will be the header of the df, meaning we
    # can access the column names
    df = pd.read_csv('adult.data.csv', sep=',',header=0, index_col=False)
    print(df)
    # print('type:', type(df))

    # How many of each race are represented in this dataset?
    # This should be a Pandas series with race names as the index labels.

    # Count the unique items of 'race'
    race_count = df['race'].value_counts()

    # What is the average age of men?
    # as_index=False outputs as a dataframe
    average_age_men_group = df.groupby('sex', as_index=True)['age'].mean()

    # This part really frustrated me because I kept getting errors

    # After some reading I decided to make average_age_men_group a series
    # so that .loc['Male'] can be used instead of .loc with an integer

    # round() function with the digits parameter lets you set # of decimals
    average_age_men = round(average_age_men_group.loc['Male'], 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors_education_mean = df['education'].value_counts(normalize=True) * 100
    percentage_bachelors = round(percentage_bachelors_education_mean.loc['Bachelors'], 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # First get just education value counts without normalization
    education_value_counts = df['education'].value_counts()

    higher_education = education_value_counts.loc[['Bachelors', 'Masters', 'Doctorate']]
    lower_education = education_value_counts.loc[~education_value_counts.index.isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    salary_df = df['salary'].value_counts(normalize=True) * 100
    higher_education_rich = round(salary_df.loc['<=50K'], 1)
    lower_education_rich = round(salary_df.loc['>50K'], 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    work_hours = df['hours-per-week']
    min_work_hours = work_hours.min()

    # What percentage of the people who work the minimum number of hours
    # per week have a salary of >50K?
    # First create a dataframe with only rows that meet criteria of the number
    # of hours worked equals the minimum work work_hours
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours]

    # Now narrow the df to a series containing only the column of 'salary'
    # Use .value_counts(normalize=True) function to return the unique freq
    # count of <=50K and >50K, while multiplying by 100 to move decimal
    # two spaces to the right
    min_work_hours_salary = num_min_workers['salary'].value_counts(
                            normalize=True) * 100
    rich_percentage = min_work_hours_salary.loc['>50K']

    # What country has the highest percentage of people that earn >50K?
    # Sort first to return a dataframe with just country and salary
    df_greater_than_50 = df[['native-country', 'salary']]

    # Obtain the values of >50K and <=50K and sort the index which will
    # alphabetize the countries
    county_salary_values = df_greater_than_50.value_counts().sort_index(ascending=True)


    # Select the rows based on >50K
    # df.loc[df['column_name'] == some_value]

    # https://www.kite.com/python/answers/how-to-generate-percentages-of-pandas-columns-in-python
    # For this section we need to keep the country and salary grouped
    # I really don't like this section because it's making me multi-index
    # and I still don't feel really comfortable with my understanding of it
    county_salary_percent = county_salary_values.groupby(
                            level='native-country').apply(
                            lambda x: 100 * x / float(x.sum()))

    # .reset_index() so we can have column header names and for neatness rename
    # int 0 column header to 'unique-values' column header
    county_salary_percent = county_salary_percent.reset_index()
    county_salary_percent = county_salary_percent.rename(columns={0 : 'unique-values'})

    # Access rows using .loc with criteria of 'salary' that is >50K
    highest_earning = county_salary_percent.loc[county_salary_percent['salary'] == '>50K']
    highest_earning = highest_earning.sort_values('unique-values', ascending=False)

    # Return the first row only under column 'native-country'
    highest_earning_country = highest_earning['native-country'].iloc[0]
    # Return the first row only under 'unique values' and round decimals to 1
    highest_earning_country_percentage = round(highest_earning['unique-values'].iloc[0], 1)

    # Identify the most popular occupation for those who earn >50K in India.

    # Return a series with only country and occupation
    country_occupation = df[['native-country', 'occupation']]
    # Value counts the Series object
    country_occupation_counts = country_occupation.value_counts()
    # Reset index so we can sort by country
    country_occupation_counts_df = country_occupation_counts.reset_index()
    # Access dataframe 
    country_occupation_counts_india = country_occupation_counts_df.loc[country_occupation_counts_df['native-country'] == 'India']

    print(country_occupation_counts_india)

    top_IN_occupation = None

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
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()
