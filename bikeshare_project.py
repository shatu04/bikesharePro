import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Ask user to specify a city, month, and day to analyze.

    Returns:
    city (str): name of the city to analyze
    month (str): name of the month to filter by, or "all" to apply no filter
    day (str): name of the day of week to filter by, or "all" to apply no filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input("Enter city (Chicago, New York City, Washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city. Please choose from Chicago, New York City, or Washington.")

    while True:
        month = input("Enter month (January to June) or 'all': ").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Invalid month. Please enter a month from January to June, or 'all'.")

    while True:
        day = input("Enter day of week or 'all': ").lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Invalid day. Please enter a valid day or 'all'.")

    return city, month, day

def load_data(city, month, day):
    """
    Load data for the specified city and filter by month and day if applicable.

    Arguments:
    city (str): name of the city
    month (str): month to filter by or "all"
    day (str): day of week to filter by or "all"

    Returns:
    df (DataFrame): filtered data
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Display statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')

    print("Most common month:", df['month'].mode()[0])
    print("Most common day of week:", df['day_of_week'].mode()[0])
    print("Most common start hour:", df['Start Time'].dt.hour.mode()[0])

def station_stats(df):
    """Display statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')

    print("Most commonly used start station:", df['Start Station'].mode()[0])
    print("Most commonly used end station:", df['End Station'].mode()[0])
    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    print("Most frequent combination of start station and end station trip:", df['Trip'].mode()[0])

def trip_duration_stats(df):
    """Display statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')

    print("Total travel time:", df['Trip Duration'].sum())
    print("Average travel time:", df['Trip Duration'].mean())

def user_stats(df):
    """Display statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')

    print("Counts of user types:\n", df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print("Counts of gender:\n", df['Gender'].value_counts())
    else:
        print("No gender data available.")

    if 'Birth Year' in df.columns:
        print("Earliest year of birth:", int(df['Birth Year'].min()))
        print("Most recent year of birth:", int(df['Birth Year'].max()))
        print("Most common year of birth:", int(df['Birth Year'].mode()[0]))
    else:
        print("No birth year data available.")

def display_data(df):
    """
    Display 5 rows of raw data at a time upon user request.

    Arguments:
    df -- DataFrame containing filtered data
    """
    start_loc = 0
    while True:
        view_data = input('\nWould you like to view 5 rows of raw data? Enter yes or no: ').lower()
        if view_data != 'yes':
            break
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        if start_loc >= len(df):
            print("You've reached the end of the data.")
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no: ').lower()
        if restart != 'yes':
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()
