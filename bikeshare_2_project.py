import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city
    while True:
        city = input("Please enter a city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please choose from chicago, new york city, or washington.")

    # Get user input for month
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Please enter a month (january to june) or 'all': ").lower()
        if month in months:
            break
        else:
            print("Invalid input. Try again.")

    # Get user input for day of week
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Please enter a day of the week or 'all': ").lower()
        if day in days:
            break
        else:
            print("Invalid input. Try again.")

    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of week, and hour
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if needed
    if month != 'all':
        df = df[df['month'] == month]

    # Filter by day of week if needed
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if not df.empty:
        print("Most common month:", df['month'].mode()[0].title())
        print("Most common day of week:", df['day_of_week'].mode()[0].title())
        print("Most common start hour:", df['hour'].mode()[0])
    else:
        print("No data to calculate time stats.")

    print("This took %.2f seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    if not df.empty:
        print("Most commonly used start station:", df['Start Station'].mode()[0])
        print("Most commonly used end station:", df['End Station'].mode()[0])

        df['Trip Combination'] = df['Start Station'] + " -> " + df['End Station']
        print("Most frequent trip combination:", df['Trip Combination'].mode()[0])
    else:
        print("No data to calculate station stats.")

    print("This took %.2f seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    if not df.empty:
        print("Total travel time:", df['Trip Duration'].sum(), "seconds")
        print("Average travel time:", df['Trip Duration'].mean(), "seconds")
    else:
        print("No data to calculate trip duration.")

    print("This took %.2f seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    if not df.empty:
        # User type counts
        print("User Types:\n", df['User Type'].value_counts().to_string())

        # Gender counts
        if 'Gender' in df.columns:
            print("\nGender:\n", df['Gender'].value_counts().to_string())
        else:
            print("\nGender data not available for this city.")

        # Birth year stats
        if 'Birth Year' in df.columns:
            print("\nEarliest year of birth:", int(df['Birth Year'].min()))
            print("Most recent year of birth:", int(df['Birth Year'].max()))
            print("Most common year of birth:", int(df['Birth Year'].mode()[0]))
        else:
            print("\nBirth year data not available for this city.")
    else:
        print("No data to calculate user stats.")

    print("This took %.2f seconds." % (time.time() - start_time))
    print('-' * 40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Thanks for using the bikeshare data explorer. Goodbye!")
            break

if __name__ == "__main__":
    main()
