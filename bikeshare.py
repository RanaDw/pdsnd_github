import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze Result.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
  
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please choose a city (chicago, new york city, washington): ").lower()
    while city not in CITY_DATA:
        print("Invalid city. Please choose from 'chicago', 'new york city', or 'washington'.")
        city = input("Please choose a city (chicago, new york city, washington): ").lower()
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please choose a month (january, february, ..., june) or 'all' for no month filter: ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print("Invalid month. Please choose a valid month or 'all'.")
        month = input("Please choose a month (january, february, ..., june) or 'all' for no month filter: ").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please choose a day of the week (monday, tuesday, ..., sunday) or 'all' for no day filter: ").lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        print("Invalid day. Please choose a valid day or 'all'.")
        day = input("Please choose a day of the week (monday, tuesday, ..., sunday) or 'all' for no day filter: ").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from the Start Time column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    # Filter by month if applicable
    if month != 'all':
        month_num = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['month'] == month_num]

    # Filter by day if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    if 'month' in df.columns:
        common_month = df['month'].mode()[0]
        print(f"Most common month: {['january', 'february', 'march', 'april', 'may', 'june'][common_month-1].title()}")

    # Display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"Most common day of week: {common_day.title()}")

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f"Most common start hour: {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"Most common start station: {common_start_station}")


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"Most common end station: {common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_combo'] = df['Start Station'] + " to " + df['End Station']
    common_combo = df['start_end_combo'].mode()[0]
    print(f"Most frequent combination of start and end station: {common_combo}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_time} seconds")

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print(f"User types:\n{user_type_counts}")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(f"Gender counts:\n{gender_counts}")


    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        earliest_birth = int(df['Birth Year'].min())
        most_recent_birth = int(df['Birth Year'].max())
        most_common_birth = int(df['Birth Year'].mode()[0])
        print(f"Earliest year of birth: {earliest_birth}")
        print(f"Most recent year of birth: {most_recent_birth}")
        print(f"Most common year of birth: {most_common_birth}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """
    Asks the user if they want to see 5 rows of data, and keeps displaying them
    in chunks of 5 until the user says 'no'.
    """
    start_loc = 0  # Initialize the starting location of the rows to show

    while True:
        # Ask the user if they want to see 5 more rows of data
        view_data = input(f"Do you want to see the next 5 rows of data? Enter 'yes' or 'no': ").lower()

        # If the user says 'yes', display the next 5 rows
        if view_data == 'yes':
            # Select the next 5 rows based on the current start_loc
            print(df.iloc[start_loc:start_loc + 5])

            # Update the start location to the next set of 5 rows
            start_loc += 5

        # If the user says 'no', stop showing data
        elif view_data == 'no':
            break

        # If the start location exceeds the available rows, stop the loop
        if start_loc >= len(df):
            print("No more data to display.")
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Ask if the user wants to view the raw data after displaying stats
        display_raw_data = input('\nWould you like to see raw data? Enter yes or no.\n').lower()
        if display_raw_data == 'yes':
            display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()